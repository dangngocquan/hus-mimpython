import math

class Parallelogram():
    def __init__(self, baseSide=4, height=2, inclination=60):
        assert baseSide > 0 and height > 0 and (0 < inclination and inclination < 180)
        self.baseSide = baseSide
        self.height = height
        self.inclonation = inclination
        
    def __repr__(self):
        return f"Parallelogram[baseSide={self.baseSide},height={self.height},inclination={self.inclonation}degrees]"
    
    def perimeter(self):
        return 2 * (self.baseSide + self.height / math.sin(math.pi/180 * self.inclonation))
    
    def area(self):
        return self.baseSide * self.height


"""1) Xây dựng class Rectangle và class Square (kế thừa từ Rectangle). 
Thiết kế các thuộc tính, phương thức có liên quan."""
class Rectangle(Parallelogram):
    def __init__(self, length=4, width=2):
        assert length > 0 and width > 0
        self.length = length
        self.width = width
        super().__init__(baseSide=length, height=width, inclination=90)
        
    def __repr__(self):
        return f"Rectangle[length={self.length},width={self.width}]"

 
class Square(Rectangle):
    def __init__(self, side=2):
        assert side > 0
        self.side = side
        super().__init__(length=side, width=side)
    
    def __repr__(self):
        return f"Square[side={self.side}]"

   
"""1') Bổ sung thêm class Rhombus và thực hiện kế thừa một cách phù hợp."""
class Rhombus(Parallelogram):
    def __init__(self, side=4, inclination=60):
        self.side = side
        super().__init__(baseSide=side, height=side*math.sin(math.pi/180 * inclination), inclination=inclination)
        
    def __repr__(self):
        return f"Rhombus[side={self.side},inclination={self.inclonation}]"
    

"""2) Thực hiện yêu cầu tương tự với class Ellipse và class Circle. Chú ý rằng việc tính chu vi 
hình ellipse là một bài toán thú vị."""
class Ellipse:
    def __init__(self, length=4, width=2):
        self.length = length
        self.width = width
    
    def __repr__(self):
        return f"Ellipse[length={self.length},width={self.width}]"
    
    def perimeter(self):
        a = self.length / 2
        b = self.length / 2
        return 2 * math.pi * math.sqrt((a*a + b*b) / 2)
    
    def area(self):
        a = self.length / 2
        b = self.width / 2
        return math.pi * a * b
    

class Circle(Ellipse):
    def __init__(self, radius=2):
        self.radius = radius
        super().__init__(length=2*radius, width=2*radius)
        
    def __repr__(self):
        return f"Circle[radius={self.radius}]"


if __name__ == '__main__':
    """Test Rectangle"""
    rect = Rectangle(length=4, width=2)
    print(rect)                 # Rectangle[length=4,width=2,coordinateTopLeft=[0, 0]]
    print(rect.perimeter())     # 12.0
    print(rect.area())          # 8
    
    """Test Square"""
    square = Square(side=6)         
    print(square)               # Square[side=6,coordinateTopLeft=[0, 0]]         
    print(square.perimeter())   # 24.0
    print(square.area())        # 36
    
    """Test Rhombus"""
    rhombus = Rhombus(side=4, inclination=90)         
    print(rhombus)               # Rhombus[firstDiagonal=8,secondDiagonal=6,coordinateTopLeft=[0, 0]]         
    print(rhombus.perimeter())   # 16.0
    print(rhombus.area())        # 16.0
    
    """Test Ellipse"""
    ellipse = Ellipse(length=8, width=6)      
    print(ellipse)               # Ellipse[length=8,width=6]        
    print(ellipse.perimeter())   # 25.132741228718345
    print(ellipse.area())        # 37.69911184307752
    
    """Test Circle"""
    circle = Circle(radius=3)     
    print(circle)               # Circle[radius=3]        
    print(circle.perimeter())   # 18.84955592153876
    print(circle.area())        # 28.274333882308138
    