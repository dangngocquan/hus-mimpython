import math
from week04_assignment02_student42_DangNgocQuan import Point

def areaTriangle(A, B, C):
    AB = A.distance(B, 'L1')
    BC = B.distance(C, 'L1')
    CA = C.distance(A, 'L1')
    p = (AB + BC + CA) / 2
    area = math.sqrt(p*(p-AB)*(p-BC)*(p-CA))
    return area

if __name__ == '__main__':
    pointA = Point(0, 0)
    pointB = Point(4, 0)
    pointC = Point(0, 3)
    print(areaTriangle(pointA, pointB, pointC))     # 6.0
    
    