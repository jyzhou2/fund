from peewee import *
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root', 'password': 'hdlnmp','port':3306})

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
