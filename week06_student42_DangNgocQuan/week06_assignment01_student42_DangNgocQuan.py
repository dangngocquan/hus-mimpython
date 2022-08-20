import time
import numpy
from random import randint

'''a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều 
(kiểu list hoặc tuple) gồm m hàng và n cột chứa các số tự nhiên ngẫu nhiên.'''
def createMatrix1(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randint(0, 1000))
        matrix.append(row)
    return matrix

'''b) Không sử dụng thư viện bổ sung, viết một hàm tính tổng các số thuộc cùng một 
cột của một bảng số cho trước.'''
def sumColumnOfMatrix1(matrix):
    ans = []
    for column in range(len(matrix[0])):
        sum = 0
        for row in range(len(matrix)):
            sum += matrix[row][column]
        ans.append(sum)
    return ans

'''c) Sử dụng kiểu dữ liệu numpy.ndarray, thực hiện yêu cầu tương tự như hai ý (a) và (b).'''
def createMatrix2(m, n):
    matrix = numpy.ndarray(shape=(m, n), dtype=int)
    return matrix

def sumColumnOfMatrix2(matrix):
    return matrix.sum(axis=0)

'''d) So sánh tốc độ thực hiện của hai hàm tính tổng các số theo cột đã cài đặt ở trên.'''
def compareTwoWays():
    matrix1 = createMatrix1(1000, 1000)
    start = time.time()
    sumColumns1 = sumColumnOfMatrix1(matrix1)
    end = time.time()
    time1 = end - start
    
    matrix2 = createMatrix2(1000, 1000)
    start = time.time()
    sumColumns2 = sumColumnOfMatrix2(matrix2)
    end = time.time()
    time2 = end - start
    
    print("time2 =", time2/time1, "time1")
    
'''e) Trả lời câu hỏi tương tự cho việc tính tổng các số thuộc cùng một hàng của bảng số.'''

if __name__ == '__main__':
    ''' a) b) '''
    matrix1 = createMatrix1(2, 3)
    print(matrix1)
    # [[915, 943, 66], [816, 622, 697]]
    sumColumns1 = sumColumnOfMatrix1(matrix1)
    print(sumColumns1)
    # [1081, 739, 1299]
    
    ''' c) '''
    matrix2 = createMatrix2(2, 3)
    print(matrix2)
    # [[-445191504        545          0]
    #  [         0          0          0]]
    sumColumns2 = sumColumnOfMatrix1(matrix2)
    print(sumColumns2)
    # [-445191504, 545, 0]
    
    ''' d) '''
    compareTwoWays()
    # time2 = 0.019769836578249843 time1
    # ==> Tốc độ khi dùng numpy nhanh hơn rất nhiều so với tự viết hàm
    
    ''' e) '''
    # Đối với việc tính tổng các số thuộc cùng một hàng trong bảng số, thì tốc độ khi dùng numpy
    # vẫn sẽ nhanh hơn so với việc tự viết hàm.