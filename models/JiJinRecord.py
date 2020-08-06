from peewee import *
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root', 'password': 'hdlnmp','port':3306})

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
