import requests
import datetime
import time
import json
import re
from models import JiJinInfo
class RealTime():

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
        url = 'http://fundgz.1234567.com.cn/js/'+str(self.jjdm)+'.js?rt='+str(timeStamp)
        response = requests.get(url)
        response_text = response.text
        print("url:"+url+" 基金代码"+self.jjdm+"return:"+response_text)
        response_text = response_text.replace('jsonpgz(', '')
        response_text = response_text.replace(');', '')
        try:
            response_json = json.loads(response_text)
        except Exception as e:
            res = {}
            res['gsl'] = ''
            res['gztime'] = ''
            return res
        # 基金代码
        jjdm = response_json['fundcode']
        # 估算涨幅
        gztime = response_json['gztime']
        gsz = response_json['gsz']
        res = {}
        res['gsl'] = gsz
        res['gztime'] = gztime
        return res

def getNumber(string):
    number = re.search("\d+(\.\d+)亿", string)  # 提取指定字符前的数字
    if number is not None:
        number = number.group()
        number = number.replace('亿', '')
        return number
    return 0

jjdm_list = JiJinInfo.select()
for i in jjdm_list:
    jjdm = i.jjdm
    jijinguimo = i.jijin_guimo
    if jijinguimo is not None:
        number = getNumber(jijinguimo)
        #开始更新数据库中基金规模数字信息
        JiJinInfo.update({JiJinInfo.guimo_number:number}).where(JiJinInfo.jjdm==jjdm).execute()
        # 开始更新gsl，最新的基金净值
        rt = RealTime(jjdm)
        res = rt.getGuSuan()
        gsl = res['gsl']
        gsl_update_time = res['gztime']
        JiJinInfo.update({JiJinInfo.guimo_number:number,JiJinInfo.gsl:gsl,JiJinInfo.gsl_update_time:gsl_update_time}).where(JiJinInfo.jjdm==jjdm).execute()


