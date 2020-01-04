#File: main.py
#Purpose: an employee payroll simulator
#Name: Jacy Yu
#Drexel ID: jy529
#Date: 5/31/19

from Employee import Employee
from Node import Node
from LinkedList import LinkedList
import sys

#menu function to print all the options
def menu():
    print("a. Add New Employee")
    print("b. Enter Hours Worked")
    print("c. Display Payroll")
    print("d. Update Employee Hourly Rate")
    print("e. Remove Employee from Payroll")
    print("f. Exit the program")

#check if the id already exists in the linked list
def checkID(LL, ID):
    for i in range(0, len(LL)):
        if ID == LL[i].getID():
            return True
    return False

#check if the number (e.g. hourly pay) is a float or not
def checkFloat(num):
    while True:
        try:
            num = float(num)
            return True
        except:
            return False

employeeList = LinkedList() #instantiate the employee linked list
running = True

#loop to keep asking for an input until the user decides to stop using the payroll
while running:
    print("\n*** CS 172 Payroll Simulator ***")
    menu()
    command = input("\nEnter your choice (letter only): ")
    if command.lower() == "a": #choice a
        name = input("Enter the new employee's name: ")
        emId = input("Enter the new employee ID: ")
        while True:
            if emId.isdigit(): #make sure the id is a valid input
                if checkID(employeeList, emId):
                    emId = input("Employee already exists, enter a different ID: ")
                else:
                    break
            else:
                emId = input("Invalid ID number, enter a different one: ")
        hrsPay = input("Enter the hourly rate: ")
        while True:
            if checkFloat(hrsPay): #make sure the hourly pay is a valid input
                hrsPay = float(hrsPay)
                if hrsPay >= 6:
                    break
            else:
                hrsPay = input("Hourly rate invalid, please enter another one: ")
        employee = Employee(name, emId, hrsPay) #create the employee object
        employeeList.append(employee) #append the employee object to the linked list
    elif command.lower() == "b": #choice b
        for i in range(0, len(employeeList)): #for loop to go through each employee to add the hours worked
            newHrsStr = "Enter hours worked for employee " + str(employeeList[i].getID()) + ": "
            newHrs = input(newHrsStr)
            while True:
                if checkFloat(newHrs): #make sure the hours worked is a valid input
                    newHrs = float(newHrs)
                    employeeList[i].setWorkHrs(newHrs)
                    break
                else:
                    newHrs = input("Invalid hours, enter different hours: ")
    elif command.lower() == "c": #choice c
        print("\n*** Payroll ***")
        for i in range(0, len(employeeList)): #for loop to print all the employee info. in the payroll
            print(employeeList[i], "\n")
    elif command.lower() == "d": #choice d
        employeeId = input("Enter the employee ID you'd like to change: ")
        if checkID(employeeList, employeeId): #check if id exists
            for i in range(0, len(employeeList)):
                if employeeId == employeeList[i].getID(): #find the id that matches
                    newPay = input("Enter the new hourly rate: ")
                    while True:
                        if checkFloat(newPay): #make sure the new hourly pay is a valid input
                            newPay = float(newPay)
                            employeeList[i].setHrsPay(newPay)
                            break
                        else:
                            newPay = input("Invalid rate, enter a different rate: ")
        else:
            print("Employee doesn't exist.")
    elif command.lower() == "e": #choice e
        employeeId = input("Enter the employee ID you'd like to remove: ")
        if not employeeList.isEmpty(): #check if the linked list is empty
            for i in range(0, len(employeeList)):
                if employeeId == employeeList[i].getID(): #match the id
                    employeeList.pop(employeeList[i]) #use pop method from employee class to remove the employee
                    print("Done.")
                    break
                else:
                    print("Employee doesn't exist.")
        else:
            print("There are no employees.")
    elif command.lower() == "f": #choice d
        running = False #break out of while loop
    else: #invalid command
        print("Command not valid.") 
        print("Please try again.")
        
print("Good bye!")
sys.exit() #exit program