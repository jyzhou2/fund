from CollectFund import CollectJijinInfo
from models.JiJinInfo import JiJinInfo
from models.JiJinTheme import JiJinTheme
from DingDingMsgDao import DingDingMsgDao
from FileCache import FileCache
import time
from LogDao import LogDao


class CollectFundEvent:
    def __init__(self):
        self.runat = '14:00:00'
        self.event_name = 'collectfundevent'

    def handle(self):
        now = time.strftime("%H:%M:%S")
        # 大于已经要执行的时间
        if now > self.runat:
            # 今天尚未执行
            if FileCache.get(self.event_name) is not None:
                return
            else:
                # 开始更新基金信息
                CollectFundEvent.updateFundInfo(self.event_name)
        else:
            return


    staticmethod
    def updateFundInfo(event_name):
        # 开始执行操作
        LogDao.saveLog('collectfund', '开始更新基金信息')
        if not JiJinInfo.table_exists():
            JiJinInfo.create_table()
        if not JiJinTheme.table_exists():
            JiJinTheme.create_table()
        model = CollectJijinInfo()
        model.handle()
        msgDao = DingDingMsgDao()
        msgDao.sendMsg('基金信息更新完成')
        LogDao.saveLog('collectfund', '基金信息更新完成')
        FileCache.put(event_name, 1, 3600 * 23)
