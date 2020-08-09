from peewee import *
import sys
sys.append('..')
from config.database import DATABASE_CONFIG
database = MySQLDatabase('test', **{'charset': 'utf8', 'use_unicode': True, 'host': DATABASE_CONFIG['host'], 'user': DATABASE_CONFIG['user'], 'password': DATABASE_CONFIG['password'],'port':DATABASE_CONFIG['port']})

class JiJinGuSuan(Model):
    jjdm = CharField(null=True)
    gsl = CharField(null=True)  # 估算涨幅
    guimo_number = CharField(null=True)  # 规模数字（亿为单位）
    gsl_update_time = CharField(null=True)  # 更新估算时间
    one_week_level = CharField(null=True)  # 一周内水平
    one_month_level = CharField(null=True)  # 一个月内水平
    three_months_level = CharField(null=True)  # 三个月水平
    six_months_level = CharField(null=True)  # 六个月水平
    gszzl = CharField(null=True)  # 六个月水平
    jijin_pic = CharField(null=True)  # 六个月水平
    recommand = CharField(null=True)  # 六个月水平
    class Meta:
        database = database
        db_table = 'dlj_jijingusuan'

    staticmethod
    def updateGusuan(jjdm,gszzl,gsl, guimo_number,gsl_update_time, one_week_level, one_month_level, three_months_level,six_months_level):
        result = JiJinGuSuan.select().where(JiJinGuSuan.jjdm == jjdm)
        if len(result) == 0:
            JiJinGuSuan.create(jjdm= jjdm, gszzl=gszzl,gsl=gsl,gsl_update_time=gsl_update_time,guimo_number=guimo_number,one_week_level=one_week_level,
                               one_month_level=one_month_level,three_months_level=three_months_level,six_months_level=six_months_level)
            print('插入操作已完成')
        else:
        # 存在记录则进行更新操作
            JiJinGuSuan.update({JiJinGuSuan.gsl: gsl,JiJinGuSuan.gsl_update_time:gsl_update_time,JiJinGuSuan.guimo_number:guimo_number,
                                JiJinGuSuan.one_week_level:one_week_level,JiJinGuSuan.one_month_level:one_month_level,
                                JiJinGuSuan.three_months_level:three_months_level,JiJinGuSuan.six_months_level:six_months_level})\
                .where(JiJinGuSuan.jjdm == jjdm).execute()
            print('更新操作已完成')
