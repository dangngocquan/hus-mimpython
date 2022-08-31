import math

class Point:
    def __init__(self, x=0, y=0):
        assert (type(x) == type(0) or type(x) == type(0.1)) and (type(y) == type(0) or type(y) == type(0.1))
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point[x={self.x},y={self.y}]"
    
    def distance(self, anotherPoint):
        return math.sqrt((self.x - anotherPoint.x)**2 + (self.y - anotherPoint.y)**2)