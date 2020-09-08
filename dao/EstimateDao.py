import requests
import datetime
import time
import json
import re

from models.JiJinInfo import JiJinInfo
from models.JiJinRecord import JiJinRecord
from models.JiJinGuSuan import JiJinGuSuan

from dao.DingDingMsgDao import DingDingMsgDao
from dao.LogDao import LogDao

msgControl = DingDingMsgDao()


class EstimateDao():

    def __init__(self, jjdm):
        self.jjdm = jjdm

    def getTodayTimeLimit(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        date += ' 14:30:00'
        # 转换成时间戳
        # 先转换为时间数组
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")

        # 转换为时间戳
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    def getGuSuan(self):
        timeStamp = self.getTodayTimeLimit()
        url = 'http://fundgz.1234567.com.cn/js/' + str(self.jjdm) + '.js?rt=' + str(timeStamp)
        response = requests.get(url)
        response_text = response.text
        LogDao.saveLog('estimate',"url:" + url + " 基金代码" + self.jjdm + "return:" + response_text)
        response_text = response_text.replace('jsonpgz(', '')
        response_text = response_text.replace(');', '')
        try:
            response_json = json.loads(response_text)
        except Exception as e:
            res = {}
            res['gsl'] = None
            res['gztime'] = None
            return res
        # 基金代码
        jjdm = response_json['fundcode']
        # 估算涨幅
        gztime = response_json['gztime']
        gsz = response_json['gsz']
        res = {}
        res['gsl'] = gsz
        res['gszzl'] = response_json['gszzl']
        res['gztime'] = gztime
        return res


class EstimateAll():
    '''
        获得基金规模的数字
    '''
    def getNumber(self,string):
        number = re.search("\d+(\.\d+)亿", string)  # 提取指定字符前的数字
        if number is not None:
            number = number.group()
            number = number.replace('亿', '')
            return number
        return 0

    def getLowerRate(self,jjdm, count_days, current_gsl):
        all_week = JiJinRecord.select().where(JiJinRecord.jjdm == jjdm).order_by(JiJinRecord.date.desc()).limit(
            count_days)
        LogDao.saveLog('estimate','总的 要求数量' + str(count_days) + "实际数量：" + str(len(all_week)))

        ids = []
        for item in all_week:
            ids.append(item.id)
        lower_day_count = JiJinRecord.select().where(
            (JiJinRecord.jjdm == jjdm) & (JiJinRecord.id in ids) & (JiJinRecord.dwjz < current_gsl)).count()
        LogDao.saveLog('estimate','比例 要求数量' + str(count_days) + "实际数量：" + str(lower_day_count))

        return lower_day_count / (len(ids))

    '''
        单个基金估算 
    '''

    def computeJiJinEstimate(self,i, times=1):
        jjdm = i.jjdm
        jijinguimo = i.jijin_guimo
        if jijinguimo is not None:
            try:
                number = self.getNumber(jijinguimo)
                # 开始更新gsl，最新的基金净值
                rt = Estimate(jjdm)
                res = rt.getGuSuan()
                gsl = res['gsl']
                if gsl is None:
                    return
                LogDao.saveLog('estimate','开始计算' + jjdm + '的值')

                gsl_update_time = res['gztime']
                gszzl = res['gszzl']
                # 更新一周内  一个月内   三个月内   六个月内水平值
                # 计算出 一周内小于当前估值的比例
                # 计算出 一个月内小于当前估值的比例
                # 计算出 三个月内小于当前估值的比例
                #    计算出 六个月内小于当前估值的比例
                one_week_level = self.getLowerRate(jjdm, 7, gsl)
                one_month_level = self.getLowerRate(jjdm, 30, gsl)
                three_months_level = self.getLowerRate(jjdm, 90, gsl)
                six_months_level = self.getLowerRate(jjdm, 180, gsl)
                JiJinGuSuan.updateGusuan(jjdm=jjdm, gszzl=gszzl, gsl=gsl, guimo_number=number,
                                         gsl_update_time=gsl_update_time, one_week_level=one_week_level,
                                         one_month_level=one_month_level, three_months_level=three_months_level,
                                         six_months_level=six_months_level)

                LogDao.saveLog('estimate',jjdm + '更新完成')

            except Exception as e:
                time.sleep(4)
                LogDao.saveLog('estimate',"重新处理" + jjdm+" err:"+e.message)

                msgControl.sendMsg("重新处理" + jjdm)
                if times < 3:
                    times = times + 1
                    self.computeJiJinEstimate(i, times)
                return


