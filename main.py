from knapsack import *
from generation import *
import random

itemList = [[7, 7], [7, 3], [9, 3], [10, 9], [1, 2], [5, 7], [6, 7], [10, 6], [2, 6], [9, 8], [4, 7], [10, 8], [5, 3], [5, 2], [3, 7], [9, 9], [3, 3], [8, 1], [6, 6], [8, 7], [7, 3], [8, 5], [9, 2], [1, 7], [10, 2], [10, 1], [8, 2], [8, 6], [1, 4], [8, 7]]
maxWeight = 100

def createItemsList(length):
    itemList = []
    for i in range(length):
        itemList.append([random.randint(1, 10), random.randint(1, 10)])
    return itemList

def createRandomKnapsack(items, maxWeight):
    ks = knapsack()
    while True:
        # Select a random item from the given list of items
        nextItem = items[random.randint(0, len(items) - 1)]

        # If nextItem brings ks over weight limit, stop
        if ks.getWeight() + nextItem[0] >= maxWeight:
            break

        # Add nextItem to knapsack
        ks.add(nextItem)
    return ks

def findNextParents(gen):
    parent1 = None
    parent2 = None

    for knap in gen.getKnapsacks():
        if parent1 == None:
            parent1 = knap
            break
        elif parent2 == None:
            print("gotcha")
            parent2 = knap
            break
        elif knap.getValue() > parent1.getValue():
            parent1 = knap
            break
        elif knap.getValue() > parent2.getValue():
            parent2 = knap
            break
    
    print("\n\n\n Parents:")    
    parent1.printOut()
    parent2.printOut()


def main():
    firstGen = generation()

    for i in range(6):
        firstGen.add(createRandomKnapsack(itemList, maxWeight))

    firstGen.printKnapsacks()

    findNextParents(firstGen)
    
        

if __name__ == "__main__":
    main()