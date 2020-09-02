from models.JiJinGuSuan import JiJinGuSuan
from RecommandFund import CurvePloy
from FileCache import FileCache
from DingDingMsgDao import DingDingMsgDao
import time
from LogDao import LogDao


class RecommandEvent:
    def __init__(self):
        self.runat = '14:00:00'
        self.event_name = 'recommandevent'

    def handle(self):
        now = time.strftime("%H:%M:%S")
        # 大于已经要执行的时间
        if now > self.runat:
            # 今天尚未执行
            if FileCache.get(self.event_name) is not None:
                return
            else:
                # 开始更新基金信息
                RecommandEvent.computeRecommand(self.event_name)
        else:
            return


    staticmethod
    def computeRecommand(event_name):
        # 开始执行操作
        LogDao.saveLog('recommand', '开始计算更新值')
        info_list = JiJinGuSuan.select()
        for info in info_list:
            LogDao.saveLog('recommand', '正在处理基金' + info.jjdm)
            mode = CurvePloy(info.jjdm, 7)
            mode.handle()
        msgDao = DingDingMsgDao()
        msgDao.sendMsg('基金推荐值计算完成')
        FileCache.put(event_name, 1, 3600 * 23)
