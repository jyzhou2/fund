'''
    筛选出当天跌幅超过2。5的基金
'''
from models.JiJinInfo import JiJinInfo
import requests
import json
import datetime
import time
from MsgDao import MsgDao


def getTodayTimeLimit():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    date += ' 14:30:00'
    # 转换成时间戳
    # 先转换为时间数组
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")

    # 转换为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp



def doGuSuan(jjdm):
    timeStamp = getTodayTimeLimit()
    url = 'http://fundgz.1234567.com.cn/js/' + str(jjdm) + '.js?rt=' + str(timeStamp)
    response = requests.get(url)
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
    gszzl = float(gszzl)
    if gszzl <=  -2:
        msg = MsgDao()
        msg.sendMsg(jjdm+'跌幅超过预警')

def jj_rate():
    jjdm_list = JiJinInfo.select()
    for i in jjdm_list:
        jjdm = i.jjdm
        doGuSuan(jjdm)

jj_rate()