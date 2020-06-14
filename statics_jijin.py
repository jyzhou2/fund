import pandas as pd
from models import JiJinRecord,JijinStatics,JiJinInfo,JiJinStaticsUpdate
import numpy as np
from peewee import DoesNotExist
class StaticsJijin():
    # 构造函数，获得基金代码
    def __init__(self,jjdm):
        self.jjdm = jjdm

    # 依次填充记录
    def handle(self, date):
        # 得到所有有基金记录的日期，进行计算
        records = JiJinRecord.select().where((JiJinRecord.jjdm==self.jjdm) & (JiJinRecord.date == date)).limit(1)

        for record in records:
            if record is not None:
                print("正在处理："+self.jjdm+" 的"+date+"的数据")
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
                -JiJinRecord.date).limit(3)
        if type == 2:  #一周
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                -JiJinRecord.date).limit(7)
        if type == 3:  #三周
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                -JiJinRecord.date).limit(21)
        if type == 4:  # 一个月
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                -JiJinRecord.date).limit(30)
        if type == 5:  # 三个月
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                -JiJinRecord.date).limit(90)
        if type == 6:  # 半年
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                -JiJinRecord.date).limit(180)
        if type == 7:
            records = JiJinRecord.select().where((JiJinRecord.jjdm == self.jjdm) & (JiJinRecord.date < date)).order_by(
                -JiJinRecord.date).limit(360)
        return records


    '''
        填充数据
    '''
    def fillAllData(self,date, type):
        try:
            # 当天没有找到记录的，则不统计当天的信息，注意get 里面的与  自条件必须用小括号括起来
            jj_record = JiJinRecord.get((JiJinRecord.date == date) & (JiJinRecord.jjdm == self.jjdm))
        except DoesNotExist as e:
            return
        try:
            record = JijinStatics.get((date==date) &  (type==type) & (jjdm==self.jjdm))
            print(self.jjdm+":"+date+"："+str(type)+"已经处理完毕")
        except DoesNotExist as e:
            incr = self.computeIncr(date,type)
            if incr == -1:
                return
            standard = self.computeStandard(date,type)
            squard = self.computeSquard(date, type)
            position_score = self.computePositionScore(date, type, jj_record)
            JijinStatics.create(jjdm=self.jjdm,incr=incr,type=type,standard=standard,squard=squard,
                                position_score=position_score,date=date)
    '''
        获得三天的增长记录
    '''
    def computeIncr(self,date,type):
        # 首先判断今天有没有数据，没有则跳过
        try:
            record = JiJinRecord.get((JiJinRecord.jjdm==self.jjdm) & (JiJinRecord.date==date))
        except DoesNotExist as e:
            return -1


        # 开始计算
        datas = self.getAllRecord(date, type)
        final_incr = 0
        for data in datas:
            dwjz = data.dwjz
            # 使用单位净值进行计算百分比
            try:
                final_incr = (float(record.dwjz) - float(dwjz)) / float(record.dwjz)
            except Exception as e:
                return -1
        return final_incr


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

'''
    进行单个基金代码的数据统计
'''
def get_all_jijin_statics(jjdm):
    print("正在处理基金"+jjdm)
    # 获得当前，基金统计的最新进度的日期
    try:
        # 获得统计进度
        statics_record = JiJinStaticsUpdate.get(JiJinStaticsUpdate.jjdm==jjdm)
        try:
            # 找到统计进度，进行大于统计进度的日期进行统计
            records = JiJinRecord.select().where((JiJinRecord.jjdm == jjdm) & (JiJinRecord.date> statics_record.date)).order_by(JiJinRecord.date).limit(1)
            record = None
            for record_first in records:
                record = record_first
                break
            if record is None:
                return
            model = StaticsJijin(jjdm)
            model.handle(record.date)

            JiJinStaticsUpdate.update({JiJinStaticsUpdate.date: record.date}).where(JiJinStaticsUpdate.jjdm == jjdm).execute()
            get_all_jijin_statics(jjdm)

        except DoesNotExist as e:
            print("找到更新记录，已经更新到最新，当前结束")
            return
    except DoesNotExist as e:
        print("未找到更新记录，开始获取最原始的基金记录")
        try:
            # 没有找到统计进度，进行基金记录的最远的日期进行统计
            records = JiJinRecord.select().where(
                JiJinRecord.jjdm == jjdm).order_by(JiJinRecord.date).limit(
                1)
            record = None
            for record_first in records:
                record = record_first
                break
            if record is None:
                return

            # 如果找到了，
            model = StaticsJijin(jjdm)
            model.handle(record.date)
            JiJinStaticsUpdate.create(jjdm=jjdm,date=record.date)
            get_all_jijin_statics(jjdm)
        except DoesNotExist as e:
            # 当前已经执行完成
            print("未找到更新记录，未找到基金记录，本次执行结束")
            return

'''
model = StaticsJijin('000001')
model.handle('2018-07-02')
exit()
'''
jj_records = JiJinInfo.select()
for item in jj_records:
    print('正在统计' + item.jjdm+'的相关信息 ')
    jjdm = item.jjdm
    get_all_jijin_statics(jjdm)








