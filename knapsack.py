from random import *

class knapsack:
    # Class Variables
    items = []
    weight = 0
    value = 0

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.weight += item[0]
        self.value += item[1]
    
    def getItems(self):
        return self.items

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def printOut(self):
        print("----------------------------------------------------------------------")
        print(self.items)
        print("Knapsack Weight: " + str(self.weight))
        print("Knapsack Value: " + str(self.value))
        print("----------------------------------------------------------------------\n\n\n")