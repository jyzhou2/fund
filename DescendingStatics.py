'''
    筛选出当天跌幅超过2。5的基金
'''
from models.JiJinInfo import JiJinInfo
import requests
import json
import datetime
import time
from DingDingMsgDao import DingDingMsgDao


class DescnedingStatics:
    '''
            获得基金更新的最近时间
    '''
    def getTodayTimeLimit(self):

        date = datetime.datetime.now().strftime('%Y-%m-%d')
        date += ' 14:30:00'
         # 转换成时间戳
        # 先转换为时间数组
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")

         # 转换为时间戳
        timeStamp = int(time.mktime(timeArray))
        return timeStamp


    '''
        获得基金的估算值
    '''
    def getEstimate(self,jjdm):
        timeStamp = self.getTodayTimeLimit()
        url = 'http://fundgz.1234567.com.cn/js/' + str(jjdm) + '.js?rt=' + str(timeStamp)
        try:
            response = requests.get(url)
        except Exception as e:
            time.sleep(3)
        response_text = response.text
        print("url:" + url + " 基金代码" + jjdm + "return:" + response_text)
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

        gszzl = response_json['gszzl']
        name = response_json['name']
        gszzl = float(gszzl)
        if gszzl <= -2:
            msg = DingDingMsgDao()
            msg.sendMsg(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ":" + name + "(" + jjdm + ')跌幅超过预警:' + str(gszzl))


    def handle(self):
        jjdm_list = JiJinInfo.select()
        for i in jjdm_list:
            jjdm = i.jjdm
            self.getEstimate(jjdm)


if __name__ == "__main__":
    hModal = DescnedingStatics()
    hModal.handle()
    msg = DingDingMsgDao()
    msg.sendMsg('跌幅统计完成')

