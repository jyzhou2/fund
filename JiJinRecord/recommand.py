# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from models import JiJinRecord,JiJinGuSuan
import pandas as pd


class CurvePloy():
    def __init__(self,jjdm,count):
        self.jjdm = jjdm
        self.count = count
        self.x = []

    def get_ploy1d(self):
        info_list = JiJinRecord.select().where(JiJinRecord.jjdm == self.jjdm).order_by(JiJinRecord.date.desc()).limit(self.count)
        y = []
        date = []
        index = 0.1
        for info in info_list:
            y.append(info.dwjz)
            date.append(index)
            index = index + 1
        y = pd.to_numeric(y)
        self.x = date
        z1 = np.polyfit(date, y, 2)  # 用2次多项式拟合
        p1 = np.poly1d(z1)  # 获得多项式
        yvals = p1(date)  # 可直接使用yvals=np.polyval(z1,xxx)
        plt.plot(date, y, '*', label='original values')
        plt.plot(date, yvals, 'r', label='polyfit values')
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.legend(loc=4)  # 指定legend在图中的位置，类似象限的位置
        plt.title('polyfitting')
        plt.show()
        plt.savefig('/home/www/wwwroot/fund_view/public/img/'+self.jjdm+'.png')
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
        print(max_pos_x)
        print(self.x)
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
        print(self.jjdm+" 推荐值是"+recommand)
        JiJinGuSuan.update({JiJinGuSuan.recommand:recommand}).where(JiJinGuSuan.jjdm == self.jjdm)

info_list = JiJinGuSuan.select()
for info in info_list:
    print('正在处理基金'+ info.jjdm)
    mode = CurvePloy(info.jjdm,7)
    mode.handle()