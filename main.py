from knapsack import *
import random

def createItemsList():
    items = []
    for i in range(30):
        items.append([random.randint(1, 10), random.randint(1, 10)])
    return items

def main():
    items = createItemsList()
    print(items)
        

if __name__ == "__main__":
    main()