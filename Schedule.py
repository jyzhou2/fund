from events.CollectFundEvent import CollectFundEvent
from events.DescendingStaticsEvent import DescendingStaticsEvent


class Schedule:
    def __init__(self):
        collect = CollectFundEvent()
        descend = DescendingStaticsEvent()
        self.events = [collect, descend]

    def handle(self):
        for item in self.events:
            print(item.handle())


if __name__ == '__main__':
    hModal = Schedule()
    hModal.handle()
