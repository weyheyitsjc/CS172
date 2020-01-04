#File: LinkedList.py
#Purpose: class that makes a linked list and all methods used with a linked list
#Name: Jacy Yu
#Drexel ID: jy529
#Date: 5/31/19
#Citation: in class code demo of LinkedList() class and lecture code by Adelaida Medlock

from Node import Node
from Employee import Employee

class LinkedList():
    def __init__(self):
        self.__head = None
        
    def getHead(self):
        return self.__head
    
    #overload len
    def __len__(self):
        nodes = 0
        current = self.__head
        while current != None:
            nodes += 1
            current = current.getNext()
        return nodes
    
    #append method to append a new node to a linked list
    def append(self, data):
        newnode = Node(data)
        if self.__head == None: #if the linked list is empty, the new node will be the head
            self.__head = newnode
        else: #traverse the linked list if it is not empty an add the node onto the end
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newnode)
            
    #pop method to remove a node from a linked list
    def pop(self, item):
        current = self.__head
        previous = None
        found = False
        
        while not found: #find the item in the linked list
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    #method to check if linked list is empty
    def isEmpty(self):
        return self.__head == None
    
    #overload index
    def __getitem__(self, index):
        if index >= len(self):
            print("Index out of bounds")
            return None
        else:
            location = 0
            current = self.__head
            while location < index:
                    location += 1
                    current = current.getNext()
            return current.getData()