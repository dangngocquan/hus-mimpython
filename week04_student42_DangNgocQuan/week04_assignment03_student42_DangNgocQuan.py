import math
from week04_assignment02_student42_DangNgocQuan import Point

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __repr__(self):
        return f"Line({self.a}*x + {self.b}*y + {self.c} = 0)"
    
    def isValidLine(self):
        return not (self.a == 0 and self.b == 0)
    
    @classmethod
    # Hàm trả về dữ liệu kiểu Tuple. Trong trường hợp một trong hai đường thẳng không hợp lệ
    # thì trả về None. Nếu hai đường thẳng trùng nhau thì sẽ trả về Tuple chứa 2 Point (2 Point 
    # khi nối với nhau sẽ tạo thành 1 đường thẳng, và chứa vô số điểm)
    def getIntersections(cls, line1, line2):
        if not line1.isValidLine() or not line2.isValidLine():
            return None
        a1 = line1.a
        b1 = line1.b
        c1 = line1.c
        a2 = line2.a
        b2 = line2.b
        c2 = line2.c
        if cls.isCoincideLines(line1, line2):
            if a1 == 0:
                point1 = Point(0.0, -c1 / b1)
                point2 = Point(1.0, -c1 / b1)
                return (point1, point2)
            else:
                point1 = Point((-c1 - b1 * 0.0 )/a1, 0.0)
                point2 = Point((-c1 - b1 * 1.0 )/a1, 1.0)
                return (point1, point2)
        elif cls.isParallelLines(line1, line2):
            return ()
        else:
            if a1 == 0:
                y = -c1 / b1
                x = (-c2 - b2 * y) / a2
                point = Point(x, y)
                return (point, )
            elif b1 == 0:
                x = -c1 / a1
                y = (-c2 - a2 * x) / b2
                point = Point(x, y)
                return (point, )
            else:
                k = b2 / b1
                x = -(c2 - k * c1) / (a2 - k*a1)
                y = (-c1 - line1.a * x) / b1
                point = Point(x, y)
                return (point, )
            
    def createLineByTwoPoints(cls, point1, point2):
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y
        if x1 == x2:
            return cls(1, 0, -x1)
        if y1 == y2:
            return cls(0, 1, -y1)
        a = y2 - y1
        b = x1 - x2
        c = x2*y1 - x1*y2
        return cls(a, b, c)
        
    @staticmethod
    def isCoincideLines(line1, line2):
         #  a2 / a1 == b2 / b1 == c2 / c1
        condition1 = line2.a * line1.b == line1.a * line2.b
        condition2 = line2.b * line1.c == line1.b * line2.c
        condition3 = line2.a * line1.c == line1.a * line2.c 
        return condition1 and condition2 and condition3
    
    def isParallelLines(line1, line2):
        #  a2 / a1 == b2 / b1 != c2 / c1
        condition1 = line2.a * line1.b == line1.a * line2.b
        condition2 = line2.b * line1.c != line1.b * line2.c
        condition3 = line2.a * line1.c != line1.a * line2.c 
        return condition1 and condition2 and condition3
    
    def isIntersectLines(line1, line2):
        #  a2 / a1 != b2 / b1
        return line2.a * line1.b != line1.a * line2.b
    
    def distanceFromPointToLine(point, line):
        if not line.isValidLine():
            return -1
        return (math.fabs(line.a * point.x + line.b * point.y + line.c)) / (
                math.sqrt(line.a ** 2 + line.b ** 2))
    
    
        
    

if __name__ == '__main__':
    '''(a) Vì sao phương trình đường thẳng có dạng y = a*x + b với a, b là hai tham số
    bất kỳ không phải là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy? 
    Đường thẳng nào không biểu diễn được qua phương trình này?'''
    # + Dạng y = a*x + b không phải là một phương trình tổng quát của một đường thẳng trong mặt 
    #   phẳng Oxy là vì phương trình này chỉ biểu diễn y theo x, mà không biểu diễn được
    #   x theo y trong đầy đủ trường hợp.
    # + Ví dụ: đường thẳng x = 0, x = 2, x = 5, ...
    
    '''(b) Xét phương trình a*x + b*y + c = 0 với a , b , c là ba tham số bất kỳ. 
    Tìm điều kiện của ba tham số a, b, c để phương trình này là phương trình tổng quát 
    của một đường thẳng trong mặt phẳng Oxy.'''
    # Điều kiện: a và b không đồng thời bằng  0
    
    '''(c) Phần khởi tạo của class Line có thể được viết như sau: 
    Nhận xét đoạn code trên.'''
    # Như đã nhận xét ở mục b), không phải bộ số (a, b, c) nào cũng tạo ra một đường thẳng hợp 
    # lệ. Đoạn code trên không thể lọc được những trường hợp không hợp lệ, vì vậy khi sử dụng, 
    # ta cần chú ý điều này để bổ sung thêm những hàm cần thiết, sử dụng cho những yêu cầu phía sau.
    
    '''(d) Viết một phương thức trong class Line để xác định (những) giao điểm của hai đường 
    thẳng (nếu có), đồng thời tự quyết định kiểu dữ liệu trả về của phương thức này.'''
    line1 = Line(0, 0, 0)                           # 0*x + 0*y + 0 = 0
    line2 = Line(0, 0, 1)                           # 0*x + 0*y + 1 = 0
    print(Line.getIntersections(line1, line2))      # None
    
    line1 = Line(1, 2, -2)                          # 1*x + 2*y - 2 = 0
    line2 = Line(2, 4, -6)                          # 2*x + 4*y - 6 = 0
    print(Line.getIntersections(line1, line2))      # ()
    
    line1 = Line(1, 0, -2)                          # 1*x + 0*y - 2 = 0
    line2 = Line(0, 1, -3)                          # 0*x + 1*y - 3 = 0
    print(Line.getIntersections(line1, line2))      # (Point(2.0, 3.0),)
    
    line1 = Line(1, 0, -2)                          # 1*x + 0*y - 2 = 0
    line2 = Line(1, -1, 0)                          # 1*x - 1*y + 0 = 0
    print(Line.getIntersections(line1, line2))      # (Point(2.0, 2.0),)
    
    line1 = Line(1, 1, -2)                          # 1*x + 1*y - 2 = 0
    line2 = Line(1, -1, 0)                          # 1*x - 1*y + 0 = 0
    print(Line.getIntersections(line1, line2))      # (Point(1.0, 1.0),)
    
    line1 = Line(1, 1, -2)                          # 1*x + 1*y - 2 = 0
    line2 = Line(2, 2, -4)                          # 1*x - 1*y + 0 = 0
    print(Line.getIntersections(line1, line2))      # (Point(2.0, 0.0), Point(1.0, 1.0))
    
    line1 = Line(1, 0, -2)                          # 1*x + 1*y - 2 = 0
    line2 = Line(2, 0, -4)                          # 1*x - 1*y + 0 = 0
    print(Line.getIntersections(line1, line2))      # (Point(2.0, 0.0), Point(2.0, 1.0))
    
    '''(e) Viết một method trong class Line để xác định khoảng cách giữa một điểm và một đường thẳng.'''
    point = Point(1, 1)                                 # Point(1.0, 1.0)
    line1 = Line(1, 0, 0)                               # 1*x + 0*y + 0 = 0
    line2 = Line(1, -1, 0)                              # 1*x - 1*y + 0 = 0
    line3 = Line(1, 1, 0)                               # 1*x + 1*y + 0 = 0
    print(Line.distanceFromPointToLine(point, line1))   # 1.0
    print(Line.distanceFromPointToLine(point, line2))   # 0.0
    print(Line.distanceFromPointToLine(point, line3))   # 1.414213562373095
    
    '''(f) Biết rằng có duy nhất một đường thẳng đi qua hai điểm phân biệt cho trước. Viết một method 
    trong class Line để khởi tạo một đường thẳng (là một instance của class Line) với tham số đầu vào 
    là hai instance của class Point. Gợi ý: Sử dụng @classmethod'''
    pointA = Point(0, 0)
    pointB = Point(1, 1)
    print(Line.createLineByTwoPoints(Line, pointA, pointB))     # Line(1*x + -1*y + 0 = 0)
    
    
    
    
    
    