from peewee import *
database = MySQLDatabase('new_jijin_info', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'root', 'password': 'hengda','port':3306})

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

    staticmethod
    def create_self(jjdm,py,name,type,quanpin):
        try:
            model = JiJinInfo.get(jjdm=jjdm)
        except Exception as e:
            JiJinInfo.create(jjdm=jjdm, py=py, name=name, type=type, quanpin=quanpin)
            return

'''
    每个基金的净值更新进度
'''
class JiJinUpdateProcess(Model):
    jjdm = CharField()
    date = CharField()
    is_processing = IntegerField(null=True, default=0)
    class Meta:
        database = database

    staticmethod
    def updateJiJinRecord(jjdm, date):
        try:
            JiJinUpdateProcess.get(jjdm = jjdm)
        except Exception as e:
            JiJinUpdateProcess.create(jjdm= jjdm, date=date)
            return
        # 存在记录则进行更新操作
        JiJinUpdateProcess.update({'date': date}).where(JiJinUpdateProcess.jjdm == jjdm).execute()

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


'''
    基金主题相关信息
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
    staticmethod
    def updateJiJinStatics(jjdm,date,type,incr,standard, squard,position_score):
        try:
            JijinStatics.get(jjdm=jjdm,date=date,type=type)
        except Exception as e:
            JijinStatics.create(jjdm=jjdm,date=date,type=type,incr=incr,standard=standard,squard=squard,position_score=position_score)

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
