'''
doctrings should explain the purpose of the class or method it is describing.
explain parameters whose usage is not immediately obvious
include examples if needed
'''

import math

class Point: 
    'Represents a point in two-dimensional geometric coordinates'
    
    def__init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y
coordinates can be speicied. If they are not, the
        point defaults to the origin.'''
        self.move(x, y)
    
    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y
        
    def reset(self):
        'Reset the point back to the geometric origin: 0, 0'
        self.move(0, 0)
        
    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.
        
        This function uses the Pythagorean Theorem to calculate
the distance between the two points. The distance is
        returned as a float."""
        
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2)
    