import datetime

class Item():

    def __init__(self, name="abc", price=0, taxable=False):
        self.__name = name
        self.__price = price
        self.__taxable = taxable #check if the item is taxable or not
        
    def __str__(self):
        return str(self.__name + "_____________________________" + '{:.2f}'.format(self.__price) + '\n')
        #price = '{:.2f}'.format(self.__price, '\n')
        #return '{:_<20}{:_>20}'.format(self.__name, price)
        
    def getPrice(self):
        return self.__price
    
    def getTax(self, tax_rate):
        if self.__taxable == True:
            return tax_rate * self.__price
        else:
            return 0.0
        
class Receipt():
    
    def __init__(self, tax_rate=0):
        self.__tax_rate = tax_rate
        self.__purchases = []
        
    def __str__(self):
        empty = ''
        empty += ('----- Receipt ' + str(datetime.datetime.now()) + ' -----\n')
        tax = 0
        total = 0
        for item in self.__purchases:
            empty += str(item)
            tax += item.getTax(self.__tax_rate)
            total += item.getPrice()
        empty += '\n\n'
        empty += ('Sub Total_____________________________'+ '{:.2f}'.format(total) + '\n')
        empty += ('Tax_____________________________' + '{:.2f}'.format(tax) + '\n')
        empty += ('Total_____________________________' + '{:.2f}'.format(tax + total) + '\n')
        return empty
                
    def addItem(self, item = 'aaa'):
        self.__purchases.append(item)
        
if __name__== '__main__':
    
    purchases = Receipt(0.07)
    
    print('Welcome to Receipt Creator')
    
    valid = 0
    additem = ''
    
    while valid == 0:
        stuffs = input('Enter Item name: ')
        costs = float(input('Enter Item Price: '))
        taxing = input('Is the item taxable (yes/no): ')
        if taxing == 'yes':
            taxing = True
        else:
            taxing = False
        itemInfo = Item(stuffs, costs, taxing)
        purchases.addItem(Item(stuffs,costs,taxing))
        additem = input('Add another item (yes/no): ')
        if additem == 'no':
            valid = 1
            
    print(purchases)
    
             
            
            
    
                
                
    