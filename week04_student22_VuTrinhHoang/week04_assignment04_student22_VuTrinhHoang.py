from week04_assignment02_student22_VuTrinhHoang import Point as p

def area(A, B, C):
    c1 = B.distance(A, 'L1')
    c2 = B.distance(C, 'L1')
    c3 = A.distance(C, 'L1')
    p1 = (c1 + c2 + c3) / 2
    return (p1 * (p1-c1) * (p1-c2) * (p1-c3)) ** (1/2)

if __name__ == '__main__':
    A = p(2, -2)
    B = p(5, 9)
    C = p(6, -3)
    
    print(area(A, B, C))