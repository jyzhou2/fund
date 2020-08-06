import sys
sys.path.append("..")
import datetime
from models import JiJinUpdateProcess,JiJinRecord
from MsgDao import SendDingDingMsg
from JiJinInfo.models import JiJinInfo
import time
import requests
import json

mode = SendDingDingMsg()
class UpdateJijinRecord():


    def getYesterday(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return yesterday

    '''
           处理所有基金
    '''

    def update_all_jijin(self):
        jjdm_list = JiJinInfo.select()
        yesterday = self.getYesterday()
        cur_hour = time.localtime().tm_hour
        for i in jjdm_list:
            print('尝试更新' + str(i.jjdm)+"的基金记录")
            models = JiJinUpdateProcess.select().where(JiJinUpdateProcess.jjdm == i.jjdm)
            if len(models) == 0:
                print('未找到更新记录，正在尝试获取信息' + str(i.jjdm))
                self.proc_single_jj(i.jjdm)
            else:
                for item in models:
                    # 如果当前执行时间在20点以后，则不予处理，如果在20点以前，如果item.date是昨天的，当前基金不予处理
                    print('更新' + str(item.date) + "之后的数据")
                    self.proc_single_jj(i.jjdm, item.date)

    '''
        更新单个基金的记录
    '''
    def proc_single_jj(self,jjdm, date=''):
        if date == '':
            date = '2019-07-01'
        url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18309366863931227072_1587472982780&fundCode=' + str(
            jjdm) + '&pageIndex=0&pageSize=500&startDate=' + str(date) + '&endDate=&_=1587472982792'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Cookie': 'name=self-define-cookies-in header',
            'Referer': 'http://fundf10.eastmoney.com/jjjz_' + jjdm + '.html',
            'Cookie': 'EMFUND1=null; EMFUND2=null; Eastmoney_Fund=001410; qgqp_b_id=bd9221f46ce16af0d470519ca90a781f; st_si=64121478995183; st_asi=delete; EMFUND0=null; EMFUND3=04-14%2021%3A49%3A53@%23%24%u56FD%u6CF0CES%u534A%u5BFC%u4F53%u884C%u4E1AETF%u8054%u63A5C@%23%24008282; EMFUND4=04-14%2021%3A50%3A11@%23%24%u56FD%u6CF0CES%u534A%u5BFC%u4F53ETF@%23%24512760; EMFUND5=04-17%2022%3A18%3A46@%23%24%u65B9%u6B63%u5BCC%u90A6%u4FDD%u9669%u4E3B%u9898%u6307%u6570%u5206%u7EA7@%23%24167301; EMFUND6=04-20%2021%3A25%3A39@%23%24%u56FD%u6295%u745E%u94F6%u7A33%u5065%u517B%u8001%28FOF%29@%23%24006876; EMFUND7=04-21%2006%3A04%3A12@%23%24%u957F%u57CE%u65B0%u5174%u4EA7%u4E1A%u6DF7%u5408@%23%24000976; EMFUND9=04-21%2020%3A32%3A38@%23%24%u535A%u65F6%u9EC4%u91D1I@%23%24000930; EMFUND8=04-21 20:42:31@#$%u4E2D%u878D%u946B%u4EF7%u503C%u6DF7%u5408A@%23%24004836; st_pvi=98230182658656; st_sp=2020-04-09%2021%3A38%3A53; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=6; st_psi=20200421204251755-0-8492747394'
        }
        try:
            response = requests.get(url, headers=headers)
        except Exception as e:
            time.sleep(10)
            response = requests.get(url, headers=headers)

        response_text = response.text
        response_text = response_text.replace('jQuery18309366863931227072_1587472982780(', '')
        response_text = response_text.replace(')', '')
        jj_jz = json.loads(response_text)

        if jj_jz is None:
            mode.sendMsg(jjdm+'未找到基金净值')
            return
        jj_data = jj_jz['Data']
        if jj_data is None:
            mode.sendMsg(jjdm + '未找到jj_data')
            return
        jj_list = jj_data['LSJZList']
        if jj_list is None:
            mode.sendMsg(jjdm + 'LSJZList')
            return
        # 倒序排列，先处理老数据，最后处理新数据
        jj_list.reverse()
        for item in jj_list:
            date = item['FSRQ']
            dwjz = item['DWJZ']
            ljjz = item['LJJZ']
            rzzl = item['JZZZL']
            JiJinRecord.updateJiJinRecord(jjdm=jjdm, date=date, dwjz=dwjz, ljjz=ljjz, rzzl=rzzl)

if not JiJinRecord.table_exists():
    JiJinRecord.create_table()

if not JiJinUpdateProcess.table_exists():
    JiJinUpdateProcess.create_table()
model=UpdateJijinRecord()
model.update_all_jijin()
mode.sendMsg('基金记录更新完成')