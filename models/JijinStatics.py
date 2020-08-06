from peewee import *
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root', 'password': 'hdlnmp','port':3306})

'''
    基金统计结果的表记录
'''
class JijinStatics(Model):
    jjdm=CharField() # 基金代码
    date = CharField() # 日期
    type = CharField() # 类型 三日  一周 三周 一个月 三个月  半年  一年
    incr = DoubleField()
    standard = CharField()# 标准差
    squard=CharField() # 方差
    position_score = DoubleField() # 当前净值所属位置

    class Meta:
        database=database
        db_table='dlj_jijinstatics'
    staticmethod
    def updateJiJinStatics(jjdm,date,type,incr,standard, squard,position_score):
        try:
            JijinStatics.get(jjdm=jjdm,date=date,type=type)
        except Exception as e:
            JijinStatics.create(jjdm=jjdm,date=date,type=type,incr=incr,standard=standard,squard=squard,position_score=position_score)
