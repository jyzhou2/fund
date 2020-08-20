from peewee import *
import sys
sys.path.append('..')
from config.database import DATABASE_CONFIG
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': DATABASE_CONFIG['host'], 'user': DATABASE_CONFIG['user'], 'password': DATABASE_CONFIG['password'],'port':DATABASE_CONFIG['port']})

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
            JiJinUpdateProcess.get(jjdm = jjdm)
        except Exception as e:
            JiJinUpdateProcess.create(jjdm= jjdm, date=date)
            return
        # 存在记录则进行更新操作
        JiJinUpdateProcess.update({'date': date}).where(JiJinUpdateProcess.jjdm == jjdm).execute()
