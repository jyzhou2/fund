from peewee import *
import sys
sys.path.append('..')
from config.database import DATABASE_CONFIG
from models.JiJinUpdateProcess import JiJinUpdateProcess
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': DATABASE_CONFIG['host'], 'user': DATABASE_CONFIG['user'], 'password': DATABASE_CONFIG['password'],'port':DATABASE_CONFIG['port']})

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
            JiJinRecord.get(jjdm = jjdm,date=date)
        except Exception as e:
            JiJinRecord.create(jjdm= jjdm, date=date,dwjz=dwjz,rzzl=rzzl, ljjz=ljjz)

        # 同时更新进度
        try:
            JiJinUpdateProcess.get(jjdm = jjdm)
        except Exception as e:
            JiJinUpdateProcess.create(jjdm= jjdm, date=date)
        # 这里进行更新
        JiJinUpdateProcess.update({'date': date}).where(JiJinUpdateProcess.jjdm == jjdm).execute()
