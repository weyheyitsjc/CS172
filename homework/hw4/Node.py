#File: Node.py
#Purpose: use the Node() class to make nodes for a linked list
#Name: Jacy Yu
#Drexel ID: jy529
#Date: 5/31/19
#Citation: in class code demo of Node() class

class Node():
    #initialize the node object with data and next node attributes
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
        
    def __str__(self):
        return str(self.__data)
        
    #getters for the data and next node
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    #setter for setting the next node
    def setNext(self, next):
        self.__next = next