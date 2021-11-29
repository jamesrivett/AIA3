from knapsack import *


class generation:
    knapsacks = []

    def __init__(self):
        pass

    def printKnapsacks(self):
        for knap in self.knapsacks:
            print("\n\n")
            print(knap.getItems())
            print("Knapsack Weight: " + str(knap.getWeight()))
            print("Knapsack Value: " + str(knap.getValue()))

    def add(self, item):
        self.knapsacks.append(item)

    def remove(self, index):
        del self.knapsacks[index]

    def clear(self):
        self.knapsacks = []