import pandas as pd
from models import JiJinRecord,JijinStatics
class StaticsJijin():
    # 构造函数，获得基金代码
    def __init__(self,jjdm):
        self.jjdm = jjdm

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
        if type == 8:
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                JiJinRecord.date).limit(360)
        return records


    '''
        填充数据
    '''
    def fillAllData(self,date, type):
        try:
            record = JijinStatics.get(date=date, type=type,jjdm=self.jjdm)
        except Exception as e:
            incr = self.computeIncr(date,type)
            standard = self.computeStandard(date,type)
            squard = self.computeSquard(date, type)
            position_score = self.computePositionScore(date, type)
            JijinStatics.create(jjdm=self.jjdm,incr=incr,type=type,standard=standard,squard=squard,position_score=position_score)
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


    '''
        获得标准差
    '''
    def computeStandard(self,date, type):
        datas = self.getAllRecord(date, type)

        return 0

    '''
        获得方差
    '''
    def computeSquard(self,date, type):
        datas = self.getAllRecord(date, type)

        return 0

    '''
        获得分位数的百分比
    '''
    def computePositionScore(self,date,type):
        datas = self.getAllRecord(date, type)

        return 0
