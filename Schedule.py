from events.CollectFundEvent import CollectFundEvent
from events.RecommandEvent import RecommandEvent
from events.DescendingStaticsEvent import DescendingStaticsEvent
from events.UpdateFundRecordEvent import UpdateFundRecordEvent
from events.EstimateEvent import EstimateEvent


class Schedule:
    def __init__(self):
        collect = CollectFundEvent()
        descend = DescendingStaticsEvent()
        recommand = RecommandEvent()
        updaterecord = UpdateFundRecordEvent()
        estiamte = EstimateEvent()
        self.events = [collect, descend,recommand,updaterecord,estiamte]

    def handle(self):
        for item in self.events:
            item.handle()


if __name__ == '__main__':
    hModal = Schedule()
    hModal.handle()
