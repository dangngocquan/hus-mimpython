import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
        
    def distance(self, point2, metric):
        if metric == 'L1':
            return math.sqrt(((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2))
        else:
            return math.fabs(self.x - point2.x) + math.fabs(self.y - point2.y)
    
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    
    def symmetry(self):
        return Point(-self.x, -self.y)    
        
if __name__ == '__main__':
    point1 = Point(5, 1)
    point2 = Point(9, 0)
    point3 = Point(0, 0)
    
    print(point1.distance(point2, 'L1'))
    print(point1.distance(point3, 'L2'))        
    
    print(point1.symmetry())
    
    print(point2)