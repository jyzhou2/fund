# coding: UTF-8
from peewee import *
import datetime
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '81.70.21.205', 'user': 'root', 'password': 'hdlnmp','port':3306})


'''
    每个基金的净值更新进度
'''
class JiJinUpdateProcess(Model):
    jjdm = CharField()
    date = CharField()
    is_processing = IntegerField(null=True, default=0)
    class Meta:
        database = database
        db_table = 'dlj_jijinupdateprocess'

    staticmethod
    def updateJiJinRecord(jjdm, date):
        try:
            JiJinUpdateProcess.get(JiJinUpdateProcess.jjdm == jjdm)
        except Exception as e:
            JiJinUpdateProcess.create(jjdm= jjdm, date=date)
            return
        # 存在记录则进行更新操作
        JiJinUpdateProcess.update({'date': date}).where(JiJinUpdateProcess.jjdm == jjdm).execute()

'''
    基金每日净值记录
'''
class JiJinRecord(Model):
    jjdm = CharField(null=True)
    date = CharField(null=True)
    dwjz = CharField(null=True)
    ljjz = CharField(null=True)
    rzzl = CharField(null=True)
    class Meta:
        database = database
        db_table='dlj_jijinrecord'

    staticmethod
    def updateJiJinRecord(jjdm, date, dwjz, ljjz, rzzl):
        try:
            JiJinRecord.get(JiJinRecord.jjdm == jjdm,JiJinRecord.date==date)
        except Exception as e:
            JiJinRecord.create(jjdm= jjdm, date=date,dwjz=dwjz,rzzl=rzzl, ljjz=ljjz)

        # 同时更新进度
        try:
            JiJinUpdateProcess.get(jjdm = jjdm)
        except Exception as e:
            JiJinUpdateProcess.create(jjdm= jjdm, date=date)
        # 这里进行更新
        JiJinUpdateProcess.update({'date': date}).where(JiJinUpdateProcess.jjdm == jjdm).execute()

