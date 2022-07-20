# Hàm giải phương trình bậc 2, trả về 1 tuple gồm các nghiệm theo thứ tự tăng dần
def solve_quadratic_equation_2(a, b, c):
    answer_tuple = ()
    if a == 0:
        if b == 0:
            if c == 0:
                pass
        else:
            answer_tuple = (-c / b, )
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            answer_tuple = (-b / (2*a), )
        elif delta > 0:
            answer_tuple = ((-b - delta**(1/2)) / (2*a), (-b + delta**(1/2)) / (2*a))
    return answer_tuple

# Hàm tìm tọa độ các điểm C thỏa mãn, trả về 1 list gồm tọa độ các điểm C [[xC1, yC1], [xC2, yC2]]
def get_list_C(xA, yA, xB, yB):
    # C(xC, yC)
    list_C = []
    AB = ((xA-xB)**2 + (yA-yB)**2) ** (1/2)
    
    if xA == xB:
        yC = (yA+yB) / 2
        C1 = [xA - AB * (3**(1/2) / 2), yC]
        C2 = [xA + AB * (3**(1/2) / 2), yC]
        list_C.append(C1)
        list_C.append(C2)
        return list_C
    else:
        # yC = k1.xC + k2
        k1 = (yA-yB) / (xB-xA)
        k2 = (yA+yB)/2 - (yA-yB)*(xA+xB) / (2*(xB-xA))
        
        # xC là nghiệm của phương trình bậc 2 có dạng a.x^2 + b.x + c = 0
        a = k1**2 + 1
        b = 2 * (-xA + k1*k2 - k1*yA)
        c = xA**2 + k2**2 + yA**2 - 2*k2*yA - AB**2
        
        xC_tuple = solve_quadratic_equation_2(a, b, c)
        for xC in xC_tuple:
            yC = k1*xC + k2
            C = [xC, yC]
            list_C.append(C)
        
        return list_C

# Hàm lấy tọa độ điểm A, B và in ra tọa độ điểm C thỏa mãn
def excute():
    # Input:    Dòng đầu tiên gồm 2 số thực xA và xB cahs nhau bởi một khoảng trắng
    #           Dòng thứ hai gồm 2 số thực xB và yB cách nhau bởi một khoảng trắng
    # Output:   In ra tọa độ các điểm C thỏa mãn
    A = input().split()
    B = input().split()
    list_C = get_list_C(int(A[0]), int(A[1]), int(B[0]), int(B[1]))
    for coordinates in list_C:
        print(coordinates)
    print()

# Main
if __name__ == '__main__':
    excute()
        
        