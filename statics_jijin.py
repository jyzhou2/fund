import pandas as pd
from models import JiJinRecord,JijinStatics
import numpy as np
class StaticsJijin():
    # 构造函数，获得基金代码
    def __init__(self,jjdm):
        self.jjdm = jjdm

    # 依次填充记录
    def handle(self):
        # 得到所有有基金记录的日期，进行计算
        records = JiJinRecord.select().where(JiJinRecord.jjdm==self.jjdm)

        for record in records:
            date = record.date
            self.fillAllData(date, 1)
            self.fillAllData(date, 2)
            self.fillAllData(date, 3)
            self.fillAllData(date, 4)
            self.fillAllData(date, 5)
            self.fillAllData(date, 6)
            self.fillAllData(date, 7)

    '''
        获得所有记录值
    '''
    def getAllRecord(self, date,type):
        if type == 1: # 三天
            records = JiJinRecord.select().where((JiJinRecord.jjdm==self.jjdm) & (JiJinRecord.date< date)).order_by(
                JiJinRecord.date).limit(3)
        if type == 2:  #一周
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(7)
        if type == 3:  #三周
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(21)
        if type == 4:  # 一个月
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(30)
        if type == 5:  # 三个月
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(90)
        if type == 6:  # 半年
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(180)
        if type == 7:
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(360)
        return records


    '''
        填充数据
    '''
    def fillAllData(self,date, type):
        try:
            # 当天没有找到记录的，则不统计当天的信息
            jj_record = JiJinRecord.get(JiJinRecord.date == date & JiJinRecord.jjdm == self.jjdm)
        except Exception as e:
            return
        try:
            record = JijinStatics.get(date==date &  type==type & jjdm==self.jjdm)
        except Exception as e:
            incr = self.computeIncr(date,type)
            standard = self.computeStandard(date,type)
            squard = self.computeSquard(date, type)
            position_score = self.computePositionScore(date, type, jj_record)
            JijinStatics.create(jjdm=self.jjdm,incr=incr,type=type,standard=standard,squard=squard,position_score=position_score,date=date)
    '''
        获得三天的增长记录
    '''
    def computeIncr(self,date,type):
        # 首先判断今天有没有数据，没有则跳过
        try:
            record = JiJinRecord.get(JiJinRecord.jjdm==self.jjdm, JiJinRecord.date==date)
        except Exception as e:
            return -1
        # 开始计算
        datas = self.getAllRecord(date, type)
        if len(datas)>=1:
            data = datas[0]
            dwjz = data.dwjz
            # 使用单位净值进行计算百分比
            return (float(record.dwjz)-float(dwjz))/float(record.dwjz)
        return 0


    '''
        获得标准差
    '''
    def computeStandard(self,date, type):
        datas = self.getAllRecord(date, type)
        data_list = []
        for item in datas:
            data_list.append(float(item.dwjz))
        data_list = np.array(data_list)
        mean = data_list.mean()
        if np.isnan(mean):
            return 0
        return mean



    '''
        获得方差
    '''
    def computeSquard(self,date, type):
        datas = self.getAllRecord(date, type)
        data_list = []
        for item in datas:
            data_list.append(float(item.dwjz))
        std = np.std(data_list,ddof=1)
        if np.isnan(std):
            return 0
        return std

    '''
        获得分位数的百分比
    '''
    def computePositionScore(self,date,type, jj_record):
        datas = self.getAllRecord(date, type)
        # 开始比对当前jj_record，在记录中datas中的顺序值
        data_list = []
        for item in datas:
            data_list.append(float(item.dwjz))
        dwjz = float(jj_record.dwjz)
        # 加入到data_list
        data_list.append(dwjz)
        # 获得dwjz所在索引
        data_list.sort()
        index = data_list.index(dwjz)
        index = index+1
        if type == 1:
            return index/3
        if type == 2:
            return index/7
        if type == 3:
            return index/21
        if type == 4:
            return index/30
        if type == 5:
            return index/90
        if type == 6:
            return index/180
        if type == 7:
            return index/360
        return 0

