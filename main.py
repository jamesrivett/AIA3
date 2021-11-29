from knapsack import *
import random

items = [[7, 7], [7, 3], [9, 3], [10, 9], [1, 2], [5, 7], [6, 7], [10, 6], [2, 6], [9, 8], [4, 7], [10, 8], [5, 3], [5, 2], [3, 7], [9, 9], [3, 3], [8, 1], [6, 6], [8, 7], [7, 3], [8, 5], [9, 2], [1, 7], [10, 2], [10, 1], [8, 2], [8, 6], [1, 4], [8, 7]]

def createItemsList():
    items = []
    for i in range(30):
        items.append([random.randint(1, 10), random.randint(1, 10)])
    return items

def main():
    knapsacks = []

        

if __name__ == "__main__":
    main()