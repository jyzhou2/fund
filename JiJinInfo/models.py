# coding: UTF-8
from peewee import *
import datetime
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root', 'password': 'hdlnmp','port':3306})

'''
    基金相关信息
'''

class JiJinInfo(Model):
    jjdm = CharField(null=True)
    py = CharField(null=True)
    name = CharField(null=True)
    type = CharField(null=True)
    quanpin = CharField(null=True)
    jijin_type = CharField(null=True)
    jijin_guimo = CharField(null=True)
    jijin_create_day = CharField(null=True)
    update_time = CharField(null=True)

    class Meta:
        database = database
        db_table = 'dlj_jijininfo'


    staticmethod

    def create_self(jjdm, py, name, type, quanpin):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        try:
            model = JiJinInfo.get(JiJinInfo.jjdm==jjdm)
            print('正在更新')
            JiJinInfo.update(
                {JiJinInfo.update_time: today, JiJinInfo.py: jjdm, JiJinInfo.name: name, JiJinInfo.type: type,
                 JiJinInfo.quanpin: quanpin}).where(
                (JiJinInfo.jjdm == jjdm)).execute()
        except DoesNotExist:
            print('正在插入')
            JiJinInfo.create(jjdm=jjdm, py=py, name=name, type=type, quanpin=quanpin, update_time = today)
        else:

            return


'''
    基金主题相关信息
'''
class JiJinTheme(Model):
    jjdm = CharField(null=True)
    theme_id = CharField(null=True)
    name = CharField(null=True)
    class Meta:
        database = database
        db_table = 'dlj_jijintheme'

    staticmethod
    def updateJiJinTheme(jjdm, name, theme_id):
        try:
            JiJinTheme.get(jjdm=jjdm, name=name)
        except Exception as e:
            JiJinTheme.create(jjdm=jjdm, name=name, theme_id=theme_id)
