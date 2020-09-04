import sys
from dao.DingDingMsgDao import DingDingMsgDao
from dao.FileCacheDao import FileCacheDao
import time
from dao.LogDao import LogDao
from dao.DescendingStaticsDao import DescnedingStaticsDao
sys.path.append('..')


class DescendingStaticsEvent:
    def __init__(self):
        self.runat = '14:20:00'
        self.event_name = 'descendingstatics'

    def handle(self):
        now = time.strftime("%H:%M:%S")
        # 大于已经要执行的时间
        if now > self.runat:
            # 今天尚未执行
            if FileCacheDao.get(self.event_name) is not None:
                return
            else:
                # 开始更新基金信息
                DescendingStaticsEvent.updateFundInfo(self.event_name)
        else:
            return


    staticmethod
    def updateFundInfo(event_name):
        # 开始执行操作
        FileCacheDao.put(event_name, 1, 3600 * 13)
        LogDao.saveLog('descendingstatics', '开始统计基金跌幅信息')
        hModal = DescnedingStaticsDao()
        hModal.handle()
        msg = DingDingMsgDao()
        msg.sendMsg('跌幅统计完成')
        LogDao.saveLog('descendingstatics', '基金跌幅统计完成')

