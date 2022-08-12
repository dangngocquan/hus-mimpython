import math

def isSquareNumber(number):
    return number == (int(math.sqrt(number))) ** 2

def isPalindromeNumber(number):
    str1 = str(number)
    lst = list(str1)
    lst.reverse()
    str2 = ''.join(lst)
    return str1 == str2

if __name__ == '__main__':
    start = 1
    number = start
    end = start * 10
    found = False
    while number <= end:
        if isPalindromeNumber(number**2):
            found = True
        if found:
            print(f"Có ít nhất 1 số nguyên trong khoảng [{start**2}, {end**2}] là {number**2} thỏa mãn.\n")
            start = end
            end = start*10
            number = start
            found = False
        number += 1
        
'''
Ý tưởng:    Lần lượt kiểm tra trong các đoạn [1, 100], [100, 10000], ... xem có số nguyên thỏa mãn vừa là số xuôi 
            ngược, vừa là số chính phương hay không. Nếu có thì sẽ tiếp tục kiểm tra các đoạn tiếp theo. Nếu trong 
            1 đoạn nào đó mà không tồn tại số thỏa mãn, vòng lặp sẽ dừng lại.

Kết quả:    Khi chạy vòng lặp trên, chương trình sẽ không ngừng lại, nó là vòng lặp vô hạn. Đây là 10 dòng đầu của Output:

Có ít nhất 1 số nguyên trong khoảng [1, 100] là 1 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [100, 10000] là 121 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [10000, 1000000] là 10201 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [1000000, 100000000] là 1002001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [100000000, 10000000000] là 100020001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [10000000000, 1000000000000] là 10000200001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [1000000000000, 100000000000000] là 1000002000001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [100000000000000, 10000000000000000] là 100000020000001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [10000000000000000, 1000000000000000000] là 10000000200000001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [1000000000000000000, 100000000000000000000] là 1000000002000000001 thỏa mãn.

Có ít nhất 1 số nguyên trong khoảng [100000000000000000000, 10000000000000000000000] là 100000000020000000001 thỏa mãn.

Nhìn vào output này, ta hoàn toàn có thể khẳng định được: Các số 1^2, 11^2, 101^2, 1001^2, ... đều là các số thỏa mãn 
đề bài, và có vô hạn số xuôi ngược đồng thời là số chính phương. Ta có thể chọn ra 1 số bất kì có dạng (1000...001)^2 (có n chữ số 0)
thỏa mãn.
100...001^2 (n chữ số 0)
= (10^(n+1) + 1)^2
= 10^(2n+2) + 2*10^(n+1) + 1
= 100...00200...001
(số này gôm 2n+3 chữ số, đầu và cuối là chữ số 1, chữ số 2 nằm ở chính giữa, vị trí n+2, các vị trí còn lại là các chữ số 0,
nên nó là số xuôi ngược)

'''
            