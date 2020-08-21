import sys
import requests
from models.JiJinInfo import JiJinInfo
from models.JiJinTheme import JiJinTheme
import re
import json
import pandas as pd
import time
from bs4 import BeautifulSoup
import datetime
import random

sys.path.append('..')


class CollectJijinInfo():
    '''
        获得基金基础信息,填充到jijininfo表中
    '''

    def collect_basic_jijin(self):
        url_main = 'http://fund.eastmoney.com/js/fundcode_search.js'
        all_fund_data = requests.get(url_main)
        fund_list = all_fund_data.text
        print(fund_list)
        fund_list = re.findall('var r = (.*])', fund_list)[0]
        fund_list = json.loads(fund_list)
        data = pd.DataFrame(fund_list)
        i = 1
        for cur_index in data.index:
            jjdm = data.loc[cur_index][0]
            py = data.loc[cur_index][1]
            name = data.loc[cur_index][2]
            type = data.loc[cur_index][3]
            quanpin = data.loc[cur_index][4]
            JiJinInfo.create_self(jjdm=jjdm, py=py, name=name, type=type, quanpin=quanpin)
            print('正在建立第' + str(i) + '个' + name + '基金信息')
            # 需要获取 基金规模， 基金类型， 基金主题，所属行业，成立日
            i = i + 1

    '''
        建立基金主题库，同时填充主题相关基金
    '''

    def buildThemeJijinKu(self):
        theme_list = self.collectAllThemes()
        for item in theme_list:
            print("正在处理主题" + item['name'] + "的相关基金信息")
            self.getJiJinForTheme(item)

    '''
        获得所有的主题
    '''

    def collectAllThemes(self):
        print("正在尝试获取所有的基金主题")
        theme_ids = []
        url = 'http://fund.eastmoney.com/daogou/#dt0;ft;rs;sd;ed;pr;cp;rt;tp;rk;se;nx;sc3y;stdesc;pi1;pn20;zfdiy;shlist'
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')  # 转换为BeautifulSoup的解析对象()里第二个参数为解析方式
        themeInfo = soup.find('dd', id='dd_tp')
        if themeInfo is None:
            return
        a_list = themeInfo.find_all('a')
        for a in a_list:
            # 获得所有的a 标签
            item = {}
            theme_id = a.attrs['id']
            theme_id = theme_id.replace('tp_', '')
            item['theme_id'] = theme_id
            item['name'] = a.get_text()
            theme_ids.append(item)
        # 开始获得其他主题
        theme_list = soup.find('dd', id='zzjjafloat')
        a_list = theme_list.find_all('a')
        for a in a_list:
            theme_id = a.attrs['id']
            theme_id = theme_id.replace('tp_', '')
            if len(theme_id) < 6:
                continue
            item = {}
            item['theme_id'] = theme_id
            item['name'] = a.get_text()
            theme_ids.append(item)
        return theme_ids

    '''
        获得单个主题下所有的基金代码，建立对应关系
    '''

    def getJiJinForTheme(slef, item):
        theme_id = item['theme_id']
        name = item['name']

        url = 'http://fund.eastmoney.com/data/FundGuideapi.aspx?dt=0&sd=&ed=&tp=' + theme_id + '&sc=3y&st=desc&pi=1&pn=20&zf=diy&sh=list&rnd=0.7974539681588224'
        response = requests.get(url)
        response.encoding = 'utf-8'
        response_text = response.text
        response_text = response_text.replace('var rankData =', '')
        json_date = json.loads(response_text)
        datas = json_date['datas']
        for fund in datas:
            jjdm = fund[0:fund.index(',')]
            JiJinTheme.updateJiJinTheme(jjdm=jjdm, theme_id=theme_id, name=name)

    '''
        获得所有基金的基金规模，创建时间等信息
    '''

    def UpdateAllJiJinOtherInfo(self, least_jjdm):
        jjdm_list = JiJinInfo.select()
        for item in jjdm_list:
            if item.jjdm < least_jjdm:
                continue
            if item.jijin_type is None or len(item.jijin_type) == 0:
                print("正在" + item.jjdm + '的基金规模等相关信息')
                self.getJijinOtherInfo(item)
                random_num = random.randint(0, 9)
                time.sleep(random_num)
            else:
                print("无需处理" + item.jjdm + '的基金规模等相关信息')

    '''
        获得基金的规模，创建时间，基金类型等信息
    '''

    def getJijinOtherInfo(self, item):
        url = 'http://fund.eastmoney.com/' + item.jjdm + '.html'
        response = requests.get(url)
        response.encoding = 'utf-8'  # 设置编码格式
        soup = BeautifulSoup(response.text, 'lxml')  # 转换为BeautifulSoup的解析对象()里第二个参数为解析方式
        fundInfo = soup.find('div', class_='infoOfFund')
        if fundInfo is None:
            return
        tables = fundInfo.find('table')
        if tables is None:
            return
        trs = tables.find_all('tr')
        if trs is None:
            return
        row_index = 0
        jijin_type = ''
        jijin_guimo = ''
        jijin_create_day = ''
        for tr in trs:
            if row_index == 0:
                tds = tr.find_all('td')
                index = 0
                for td in tds:
                    if index == 0:
                        jijin_type = td.get_text()
                        jijin_type = jijin_type.replace("基金类型：", "")
                        index = index + 1
                        print(jijin_type)
                        continue
                    if index == 1:
                        jijin_guimo = td.get_text()
                        jijin_guimo = jijin_guimo.replace("基金规模：", "")
                        index = index + 1
                        print(jijin_guimo)
                row_index = row_index + 1
            if row_index == 1:
                tds = tr.find_all('td')
                index = 0
                for td in tds:
                    if index == 0:
                        jijin_create_day = td.get_text()
                        jijin_create_day = jijin_create_day.replace("成 立 日：", "")
                        index = index + 1
            # 开始更新信息
            item.jijin_type = jijin_type
            item.jijin_guimo = jijin_guimo
            item.jijin_create_day = jijin_create_day
            item.save()

    '''
        更新所有的基金信息,可以一个月或者一周处理一次
    '''

    def handle(self):
        # 首先进行处理,建立标准的基金库
        # self.collect_basic_jijin()
        # 完善基金信息，包括规模，创建时间，基金类型等
        self.UpdateAllJiJinOtherInfo('')
        # 获得所有主题
        self.buildThemeJijinKu()


if __name__ == '__main__':
    if not JiJinInfo.table_exists():
        JiJinInfo.create_table()
    if not JiJinTheme.table_exists():
        JiJinTheme.create_table()

    model = CollectJijinInfo()
    model.handle()
