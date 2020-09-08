import sys
from dao.EstimateDao import EstimateDao
from models.JiJinInfo import JiJinInfo
from models.JiJinGuSuan import JiJinGuSuan
from dao.DingDingMsgDao import DingDingMsgDao
from dao.FileCacheDao import FileCacheDao
import time
from dao.LogDao import LogDao
sys.path.append('..')
msgControl = DingDingMsgDao()

class EstimateEvent():
    def __init__(self):
        self.runat = '01:00:00'
        self.event_name = 'estimate'

    def handle(self):
        now = time.strftime("%H:%M:%S")
        # 大于已经要执行的时间
        if now > self.runat:
            # 今天尚未执行
            if FileCacheDao.get(self.event_name) is not None:
                return
            else:
                # 开始更新基金信息
                EstimateEvent.estimate(self.event_name)
        else:
            return

    staticmethod

    def estimate(event_name):
        JiJinGuSuan.delete().execute()
        jjdm_list = JiJinInfo.select()
        for i in jjdm_list:
            hModal = EstimateDao()
            hModal.computeJiJinEstimate(i)
        msgControl.sendMsg('基金估算信息统计完成')