# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from models import JiJinRecord
import pandas as pd


class CurvePloy():
    def __init__(self,jjdm,count):
        self.jjdm = jjdm
        self.count = count

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
        z1 = np.polyfit(date, y, 2)  # 用3次多项式拟合
        p1 = np.poly1d(z1)
        print(p1)

mode = CurvePloy('000004',7)
mode.get_ploy1d()