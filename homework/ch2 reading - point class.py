import math

''' #making a class
class Point:
    def __init__(self, x, y):
        self.move(x,y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)
        
    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#how to use it:

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1))

point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
'''

'''
class Point:
    def __init__(self, x, y):
        self.move(x, y)
        
    def move(self, x, y):
        self.x = x
        self.y = y
        
    def reset(self):
        self.move(0, 0)
        
#constructing a point // instantiating the class so it will work

point = Point(3, 5)
print(point.x, point.y)
'''

'''
class Point:
    def __init__(self, x = 0, y = 0): #set parameters to something default
        self.move(x, y)               #don't need to put in all values if you don't want to 
'''
