from UpdateFundRecord import UpdateFundRecord
from DingDingMsgDao import DingDingMsgDao
from FileCache import FileCache
from models.JiJinRecord import JiJinRecord
from models.JiJinRecord import JiJinUpdateProcess
import time
from LogDao import LogDao


class UpdateFundRecordEvent:
    def __init__(self):
        self.runat = '14:00:00'
        self.event_name = 'updatefundrecordevent'

    def handle(self):
        now = time.strftime("%H:%M:%S")
        # 大于已经要执行的时间
        if now > self.runat:
            # 今天尚未执行
            if FileCache.get(self.event_name) is not None:
                return
            else:
                # 开始更新基金信息
                UpdateFundRecordEvent.updateFundRecord(self.event_name)
        else:
            return

    staticmethod

    def updateFundRecord(event_name):
        # 开始执行操作
        FileCache.put(event_name, 1, 3600 * 13)
        LogDao.saveLog('updatefundrecord', '开始更新基金记录')
        if not JiJinRecord.table_exists():
            JiJinRecord.create_table()

        if not JiJinUpdateProcess.table_exists():
            JiJinUpdateProcess.create_table()

        mode = DingDingMsgDao()
        model = UpdateFundRecord()
        model.update_all_jijin()
        mode.sendMsg('基金记录更新完成')
