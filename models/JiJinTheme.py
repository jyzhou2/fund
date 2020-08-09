from peewee import *
import sys
sys.append('..')
from config.database import DATABASE_CONFIG
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': DATABASE_CONFIG['host'], 'user': DATABASE_CONFIG['user'], 'password': DATABASE_CONFIG['password'],'port':DATABASE_CONFIG['port']})


'''
    基金主题相关信息
'''
class JiJinTheme(Model):
    jjdm = CharField(null=True)
    theme_id = CharField(null=True)
    name = CharField(null=True)
    class Meta:
        database = database
        db_table='dlj_jijintheme'


    staticmethod
    def updateJiJinTheme(jjdm, name, theme_id):
        try:
            JiJinTheme.get(jjdm=jjdm, name=name)
        except Exception as e:
            JiJinTheme.create(jjdm=jjdm, name=name, theme_id=theme_id)
