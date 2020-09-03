from peewee import *
import sys
sys.path.append('..')
from config.database import DATABASE_CONFIG
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': DATABASE_CONFIG['host'], 'user': DATABASE_CONFIG['user'], 'password': DATABASE_CONFIG['password'],'port':DATABASE_CONFIG['port']})

'''
    基金相关信息
'''


class JiJinInfo(Model):
    jjdm = CharField(null=True)
    py = CharField(null=True)
    name = CharField(null=True)
    type = CharField(null=True)
    quanpin = CharField(null=True)
    status = CharField(null=True)
    jijin_type = CharField(null=True)
    jijin_guimo = CharField(null=True)
    jijin_create_day = CharField(null=True)

    class Meta:
        database = database
        db_table = 'dlj_jijininfo'

    staticmethod

    def create_self(jjdm, py, name, type, quanpin):
        try:
            model = JiJinInfo.get(jjdm=jjdm)
        except Exception as e:
            JiJinInfo.create(jjdm=jjdm, py=py, name=name, type=type, quanpin=quanpin)
            return

    staticmethod

    def alterFundStatus(jjdm, status):
        JiJinInfo.update({'status': status}).where(JiJinInfo.jjdm == jjdm).execute()

