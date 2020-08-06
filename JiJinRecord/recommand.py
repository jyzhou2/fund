# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from models import JiJinRecord,JiJinGuSuan
from warn import SendDingDingMsg
import pandas as pd
import os
import time

msgControl = SendDingDingMsg()
class CurvePloy():
    def __init__(self,jjdm,count):
        self.jjdm = jjdm
        self.count = count
        self.x = []

    def get_ploy1d(self):
        # 获取最近7天的数据，然后再倒序输出
        raw_info_list = JiJinRecord.select().where(JiJinRecord.jjdm == self.jjdm).order_by(JiJinRecord.date.desc()).limit(self.count)
        # 获得record_id
        recordid = []
        for tmp_item in raw_info_list:
            recordid.append(tmp_item.id)
        info_list = JiJinRecord.select().where(JiJinRecord.id.in_(recordid)).order_by(JiJinRecord.date.asc())
        # 进行倒序操作
        print(info_list)

        y = []
        x_index = []
        date = []
        index = 0.1
        for info in info_list:
            y.append(info.dwjz)
            ans_time_stamp = time.mktime(time.strptime(info.date, "%Y-%m-%d"))
            struct_time = time.localtime(ans_time_stamp)  # 得到结构化时间格式
            now_time = time.strftime("%m-%d", struct_time)
            date.append(now_time)
            x_index.append(index)
            index = index + 1
        y = pd.to_numeric(y)
        self.x = x_index
        z1 = np.polyfit(x_index, y, 2)  # 用2次多项式拟合
        p1 = np.poly1d(z1)  # 获得多项式
        yvals = p1(x_index)  # 可直接使用yvals=np.polyval(z1,xxx)
        plt.plot(date, y, '*', label='original values')
        plt.plot(date, yvals, 'r', label='polyfit values')
        plt.xlabel('date')
        plt.ylabel('y axis')
        plt.legend(loc=4)  # 指定legend在图中的位置，类似象限的位置
        plt.title(self.jjdm)
        #plt.show()
        '''
            文件如果存在
        '''
        if os.path.exists('/home/www/wwwroot/fund/fundstatics/bootstrapvue-demo/dist/'+self.jjdm+'.png'):
            os.remove('/home/www/wwwroot/fund/fundstatics/bootstrapvue-demo/dist/'+self.jjdm+'.png')
        plt.savefig('/home/www/wwwroot/fund/fundstatics/bootstrapvue-demo/dist/'+self.jjdm+'.png')
        '''
            清空画布
        '''
        plt.clf()  # 清图。
        plt.cla()  # 清坐标轴。
        plt.close()  # 关窗口
        # 获得 a b c
        c = p1[0]
        b = p1[1]
        a = p1[2]
        return [a,b,c]

    def get_recommand(self,a,b,c):
        if a>0:
            return 0
        recommand = 0;
        max_pos_x = 0-(b/(2*a))
       # print(max_pos_x)
       # print(self.x)
        for cur_x in self.x:
            if max_pos_x < cur_x:
                recommand = recommand+1

        return recommand

        # 如果定点坐标小于  样本数据x坐标的最小值，则表示一直在下跌，推荐值是样本数量的个数

        # 如果定点坐标 处于 样本数据x坐标的中间，则推荐值样本数据x坐标中大于max_pos_x的个数
        # 如果顶点坐标大于 样本数据x坐标的最大值， 则表示处于上升期，推荐值是 0

    def handle(self):
        result = self.get_ploy1d()
        a = result[0]
        b = result[1]
        c = result[2]
        recommand = self.get_recommand(a,b,c)
        print(self.jjdm+" 推荐值是"+ str(recommand))
        JiJinGuSuan.update({JiJinGuSuan.recommand:recommand,JiJinGuSuan.jijin_pic:'http://81.70.21.205/'+self.jjdm+".png"}).where(JiJinGuSuan.jjdm == self.jjdm).execute()

info_list = JiJinGuSuan.select()
for info in info_list:
    print('正在处理基金'+ info.jjdm)
    mode = CurvePloy(info.jjdm,7)
    mode.handle()
msgControl.sendMsg('基金估算完成')