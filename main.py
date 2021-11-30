from knapsack import *
from generation import *
import random

itemList = [[7, 7], [7, 3], [9, 3], [10, 9], [1, 2], [5, 7], [6, 7], [10, 6], [2, 6], [9, 8], [4, 7], [10, 8], [5, 3], [5, 2], [3, 7], [9, 9], [3, 3], [8, 1], [6, 6], [8, 7], [7, 3], [8, 5], [9, 2], [1, 7], [10, 2], [10, 1], [8, 2], [8, 6], [1, 4], [8, 7]]
maxWeight = 100

# Used once to generate itemList
def createItemsList(length):
    itemList = []
    for i in range(length):
        itemList.append([random.randint(1, 10), random.randint(1, 10)])
    return itemList

# Creates a knapsack with random values from the itemList until weight almost exceeds max weight
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

# Determine which two members of the generation have the highest value
def findNextParents(gen):
    parent1 = None
    parent2 = None

    for knap in gen.getKnapsacks():
        if parent1 == None:
            parent1 = knap
            continue
        elif knap.getValue() > parent1.getValue():
            parent2 = parent1
            parent1 = knap
            continue
        elif parent2 == None:
            parent2 = knap
            continue
        elif knap.getValue() > parent2.getValue():
            parent2 = knap
            continue
    
    return [parent1, parent2]

# Creates two offspring based on two parents and a randomly-selected crossover index
def crossover(parents):
    offspring1 = knapsack()
    offspring2 = knapsack()
    parent1Items = parents[0].getItems()
    parent2Items = parents[1].getItems()
    crossIndex = None

    # Determine crossover index
    if len(parent1Items) <= len(parent2Items):
        crossIndex = random.randint(0, len(parent1Items) - 1)
    elif len(parent2Items) < len(parent1Items):
        crossIndex = random.randint(0, len(parent2Items) - 1)    

    # Append from parents to offspring, switching at crossIndex, ignoring index errors as one will run out sooner than the other
    for i in range(crossIndex):
        offspring1.add(parent1Items[i])
        offspring2.add(parent2Items[i])
    for i in range(crossIndex, len(parent1Items)):
        try:
            offspring1.add(parent2Items[i])
        except IndexError:
            pass
        try:
            offspring2.add(parent1Items[i])
        except IndexError:
            pass
    return [offspring1, offspring2]

def main():
    firstGen = generation()

    for i in range(6):
        firstGen.add(createRandomKnapsack(itemList, maxWeight))

    firstGen.printKnapsacks()

    parents = findNextParents(firstGen)
    offsprings = crossover(parents)
    print("offspring:")
    for offspring in offsprings:
        offspring.printOut()

    
    
        

if __name__ == "__main__":
    main()