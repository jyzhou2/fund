from events.CollectFundEvent import CollectFundEvent
from events.RecommandEvent import RecommandEvent
from events.DescendingStaticsEvent import DescendingStaticsEvent
from events.UpdateFundRecordEvent import UpdateFundRecordEvent


class Schedule:
    def __init__(self):
        collect = CollectFundEvent()
        descend = DescendingStaticsEvent()
        recommand = RecommandEvent()
        updaterecord = UpdateFundRecordEvent()
        self.events = [collect, descend,recommand,updaterecord]

    def handle(self):
        for item in self.events:
            print(item.handle())


if __name__ == '__main__':
    hModal = Schedule()
    hModal.handle()
