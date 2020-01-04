#File: Employee.py
#Purpose: class to make an employee object
#Name: Jacy Yu
#Drexel ID: jy529
#Date: 5/31/19

class Employee():
    #initialize the attributes of an employee object
    def __init__(self, name, emId, hrsPay = 6, workHrs = 0, grossWage = 0):
        self.__name = name
        self.__id = emId
        self.__workHrs = float(workHrs)
        self.__hrsPay = float(hrsPay)
        self.__grossWage = float(grossWage)
        
    #getters for ID, hourly pay, and hours worked
    def getID(self):
        return self.__id
    
    def getHrsPay(self):
        return self.__hrsPay
    
    def getWorkHrs(self):
        return self.__workHrs
    
    #setters for hours worked and hourly pay
    def setWorkHrs(self, newHrs):
        self.__workHrs = newHrs
        self.__grossWage = newHrs * self.__hrsPay #calculate and set the gross wage everytime the hourly pay is changed
    
    def setHrsPay(self, newPay):
        self.__hrsPay = newPay
        self.__grossWage = newPay * self.__workHrs #calculate and set the gross wage everytime the hours worked is changed
    
    #overload str to print a description of the employee object
    def __str__(self):
        emInfo = ""
        emInfo += "Name: " + self.__name + "\n" + "Employee ID: " + str(self.__id) + "\n" + "Hours Worked: " + str(self.__workHrs) + "\n" + "Hourly Pay: " + str(self.__hrsPay) + "\n" + "Gross Wages: " + str(self.__grossWage)
        return emInfo