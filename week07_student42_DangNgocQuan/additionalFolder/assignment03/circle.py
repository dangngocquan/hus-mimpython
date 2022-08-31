import math
from .point import Point

class Circle:
    def __init__(self, center=Point(0, 0), radius=2):
        assert radius > 0
        self.center = center
        self.radius = radius
        
    def __repr__(self):
        return f"Circle[center={self.center},radius={self.radius}]"
    
    def perimeter(self):
        return math.pi * 2 * self.radius
    
    def area(self):
        return math.pi * self.radius * self.radius