from random import *

class knapsack:
    # Class Variables
    items = []
    weight = 0
    value = 0

    def __init__(self):
        pass

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