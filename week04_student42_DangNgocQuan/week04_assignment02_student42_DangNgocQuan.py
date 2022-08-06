import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, anotherPoint, metric):
        if metric == 'L1':
            return ((self.x - anotherPoint.x) ** 2
                + (self.y - anotherPoint.y) ** 2) ** (1/2)
        elif metric == 'L2':
            return math.fabs(self.x - anotherPoint.x) + math.fabs(self.y - anotherPoint.y)
        else:
            return None
    
    def symmetricPoint(self):
        return Point(-self.x, -self.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
        
if __name__ == '__main__':
    '''1. Thiết kế phần khởi tạo của class Point (chọn tên thuộc tính phù hợp) và khởi tạo một số 
    instance của class này.'''
    pointA = Point(1, 1)
    pointB = Point(0, 0)
    
    '''2. Viết hàm distance() thuộc class Point để tính khoảng cách Euclid (hay còn gọi là chuẩn L2) 
    giữa hai instance của class Point.'''
    '''3. Bổ sung tham số metric (nhận giá trị là một str) trong hàm distance() vừa viết để tính 
    khoảng cách giữa hai điểm theo một trong hai metric: khoảng cách Euclid (chuẩn L2) hoặc khoảng cách 
    Manhattan (chuẩn L1).'''
    print(pointA.distance(pointB, 'L1'))        # 1.4142135623730951
    print(pointA.distance(pointB, 'L2'))        # 2.0
    
    '''4. Viết một method để tạo một điểm đối xứng với một điểm cho trước qua gốc tọa độ. Thực hiện yêu 
    cầu này bằng một trong ba cách dưới đây:'''
    print(pointA.symmetricPoint())      # Point(-1, -1)
    
    '''5. Bổ sung hàm __repr__() cho class Point.'''
    print(pointA.__repr__())        # Point(1, 1)