from peewee import *
import datetime
database = MySQLDatabase('new_jijin_info', **{'charset': 'utf8', 'use_unicode': True, 'host': '192.168.70.205', 'user': 'root', 'password': 'hengda','port':3306})

'''
    ??????
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

    staticmethod

    def create_self(jjdm, py, name, type, quanpin):
        model = JiJinInfo.select().where(JiJinInfo.jjdm==jjdm)
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        if len(model) == 0:
            JiJinInfo.create(jjdm=jjdm, py=py, name=name, type=type, quanpin=quanpin, update_time = today)
            return


'''
    ????????
'''
class JiJinTheme(Model):
    jjdm = CharField(null=True)
    theme_id = CharField(null=True)
    name = CharField(null=True)
    class Meta:
        database = database

    staticmethod
    def updateJiJinTheme(jjdm, name, theme_id):
        try:
            JiJinTheme.get(jjdm=jjdm, name=name)
        except Exception as e:
            JiJinTheme.create(jjdm=jjdm, name=name, theme_id=theme_id)
