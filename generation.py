class generation:
    knapsacks = []

    def __init__(self):
        pass

    def getKnapsacks(self):
        return self.knapsacks

    def add(self, item):
        self.knapsacks.append(item)

    def remove(self, index):
        del self.knapsacks[index]

    def clear(self):
        self.knapsacks = []