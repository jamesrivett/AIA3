from random import *

class knapsack:
    # Class Variables
    items = []
    weight = 0

    def add(self, item):
        self.items.append(item)
        self.weight += item[0]
    
    def getItems(self):
        return self.items

    def getWeight(self):
        return self.weight