import random
from BST import *
import time
import matplotlib.pyplot as plt

def populate(n):
    randomList = []
    bst = BST()
    
    for i in range(0, n):
        randomInt = random.randint(0, n)
        randomList.append(randomInt)
        bst.append(randomInt)
        
    return [randomList, bst]

def checkList(l, i):
    if i in l:
        return True
    else:
        return False
    
if __name__ == "__main__":

    listI = []
    regTimes = []
    bstTimes = []
    
    for i in range(1, 10000, 1000):
        listI.append(i)
        population = populate(i)
        myList = population[0]
        bst = population[1]
        
        time1 = time.time()
            
        check = 0
        for i in myList:
            if checkList(myList, i):
                check += 1

        time2 = time.time()
            
        bstCheck = 0
        for i in myList:
            if bst.isin(i):
                bstCheck += 1
        
        time3 = time.time()
            
        lTimeChange = time2 - time1
        regTimes.append(lTimeChange)
            
        bstTimeChange = time3 - time2 
        bstTimes.append(bstTimeChange)
        
        #print(i, lTimeChange)
        #print(i, bstTimeChange)
        
    plt.plot(listI, regTimes, label = "List Search")
    plt.plot(listI, bstTimes, label = "BST Search")
    
    plt.legend()
    plt.show()