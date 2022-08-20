import numpy
from matplotlib import pyplot

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def plot(self):
        x1 = numpy.linspace(self.x-1, self.x+1, 11)
        f1 = lambda x : x - x + self.y
        y1 = f1(x1)
        y2 = numpy.linspace(self.y-1, self.y+1, 11)
        f2 = lambda y : y - y + self.x
        x2 = f2(y2)
        pyplot.figure(figsize=(5,5))
        pyplot.plot(x1, y1, '-', color='blue', label="Point")
        pyplot.plot(x2, y2, '-', color='blue', label="Point")
        pyplot.xlabel("x", fontsize="14")
        pyplot.ylabel("y", fontsize="14")
        pyplot.title("Point")
        pyplot.savefig(f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment03\\point_{self.x}_{self.y}.png")
        pyplot.show()
   
class Line:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        
    def plot(self):
        x = numpy.linspace(self.pointA.x, self.pointB.x, 11)
        y = numpy.linspace(self.pointA.y, self.pointB.y, 11)
        pyplot.figure(figsize=(5,5))
        pyplot.plot(x, y, '-', color='blue', label="Line")
        pyplot.xlabel("x", fontsize="14")
        pyplot.ylabel("y", fontsize="14")
        pyplot.legend(fontsize=14)
        pyplot.title("Line")
        pyplot.savefig(f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment03\\line_{self.pointA.x}_{self.pointA.y}_{self.pointB.x}_{self.pointB.y}.png")
        pyplot.show()
        
class Circle:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius
        
    def plot(self):
        r = self.radius
        center = self.point
        x = numpy.linspace(center.x - r, center.x + r, 1001)
        f1 = lambda x: (r**2 - (x-center.x)**2)**(1/2)
        y1 = f1(x)
        f2 = lambda x: -(r**2 - (x-center.x)**2)**(1/2)
        y2 = f2(x)
        pyplot.figure(figsize=(5,5))
        pyplot.plot(x, y1, '-', color='blue', label="Circle")
        pyplot.plot(x, y2, '-', color='blue')
        pyplot.xlabel("x", fontsize="14")
        pyplot.ylabel("y", fontsize="14")
        pyplot.legend(fontsize=14)
        pyplot.title("Circle")
        pyplot.savefig(f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment03\\circle_{center.x}_{center.y}_{r}.png")
        pyplot.show()
    
if __name__ == '__main__':
    point1 = Point(2, 3)
    point1.plot()
    line1 = Line(Point(1,1), Point(2,3))
    line1.plot()
    circle1 = Circle(Point(5, 5), radius=10)
    circle1.plot()