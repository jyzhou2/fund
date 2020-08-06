from peewee import *
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root', 'password': 'hdlnmp','port':3306})


'''
    基金统计更新进度
'''
class JiJinStaticsUpdate(Model):
    jjdm = CharField()
    date = CharField()
    staticmethod
    def updateJiJinStatics(jjdm, date):
        try:
            JiJinStaticsUpdate.get((JiJinStaticsUpdate.jjdm == jjdm) & (JiJinStaticsUpdate.date == date) )
        except Exception as e:
            JiJinStaticsUpdate.create(date = date, jjdm = jjdm)
        JiJinStaticsUpdate.update({JiJinStaticsUpdate.date: date}).where((JiJinStaticsUpdate.jjdm == jjdm) ).execute()

    class Meta:
        database = database
        db_table='dlj_jijinstaticsupdate'
