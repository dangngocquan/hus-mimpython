import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def isPrime(number):
    for i in range(2, round(math.sqrt(number)) + 1):
        if number%i == 0:
            return False
    return number > 1

if __name__ == '__main__':
    """(a) Viết một hàm tính ước chung lớn nhất của hai số tự nhiên sử dụng thuật toán Euclid."""
    print(gcd(100, 115))    # 5
    print(gcd(23, 9))       # 1
    print(gcd(12, 24))      # 12
    
    
    """(b) Đặt giá trị xác suất cần tìm là P. Tính giá trị của P bằng một trong hai cách:
            + Lấy ngẫu nhiên hai số trong tập hợp đã cho rồi kiểm tra tính nguyên tố cùng nhau của chúng.
            + Đếm số cặp số nguyên tố cùng nhau trong tất cả cặp số có thể chọn được từ tập số đã cho."""
    # Giá trị xác suất P cần tìm sẽ có công thức: P = (1 - 1/p1^2)*(1 - 1/p2^2)*... với p1, p2, ... là các 
    # số nguyên tố nằm trong khoảng [1, N] (N trong bài này là 10^6)
    # Các bạn có thể xem chi tiết công thức này ở trên Internet, mình đã tham khảo công thức tính ở link này:
    # https://tuanminh1988.wordpress.com/2009/05/03/xac-suat-hai-so-nguyen-duong-nguyen-to-cung-nhau/
    
    P = 1
    for number in range(2, 1000001):
        if isPrime(number):
            P *= (1 - 1/(number**2))
    print(P)                    # 0.6079271430567112
    
    """(c) Tìm mối liên hệ giữa giá trị của P và π. Gợi ý: P≈a/π^b với a,b là hai số dương."""
    # a = 6 và b = 2, tức là P ≈ 6 / pi^2
    print(6 / (math.pi ** 2))   # 0.6079271018540267
    