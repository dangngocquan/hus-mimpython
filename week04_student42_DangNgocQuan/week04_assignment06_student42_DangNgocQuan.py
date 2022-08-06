import math
from week04_assignment02_student42_DangNgocQuan import Point

class Circle:
    def __init__(self, centerPoint, radius):
        self.centerPoint = centerPoint
        self.radius = radius
        
    def __repr__(self):
        return f"Circle({self.centerPoint}, {self.radius})"
    
    def compareTo(self, anotherCircle):
        if self.radius == anotherCircle.radius:
            return 0
        elif self.radius < anotherCircle.radius:
            return -1
        else:
            return 1
    
    def getArea(self):
        r = self.radius
        return math.pi * r * r
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    cirlce1 = Circle(Point(0, 0), 5)
    cirlce2 = Circle(Point(1, 1), 4)
    print(cirlce1.getArea())            # 78.53981633974483
    print(cirlce1.getPerimeter())       # 31.41592653589793
    print(cirlce2.getArea())            # 50.26548245743669
    print(cirlce2.getPerimeter())       # 25.132741228718345
    print(cirlce1.compareTo(cirlce2))   # 1
    print(cirlce2.compareTo(cirlce1))   # -1
    