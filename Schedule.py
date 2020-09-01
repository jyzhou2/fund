
class Schedule:
    def __init__(self):
        self.events = []

    def handle(self):

        for item in self.events:
            print(item.handle())
