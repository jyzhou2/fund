from peewee import *
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
