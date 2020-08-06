from peewee import *
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root', 'password': 'hdlnmp','port':3306})


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
