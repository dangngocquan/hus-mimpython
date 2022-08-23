import numpy
import time

def countZerosHeadingOfRow(tempMatrix, row):
    count = 0
    for element in tempMatrix[row]:
        if element == 0.0:
            count += 1
        else:
            return count
    return count

def correctOrderRows(tempMatrix, rowStart, rowEnd):
    countZeros = numpy.array([countZerosHeadingOfRow(tempMatrix, row) for row in range(tempMatrix.shape[0])])
    for turn in range(rowEnd-rowStart+1):
        for row in range(rowStart, rowEnd):
            if countZeros[row] > countZeros[row+1]:
                tempMatrix[[row, row+1]] = tempMatrix[[row+1, row]]

def gauss(matrix):
    matrix1 = matrix.astype('float64')
    correctOrderRows(matrix1, 0, matrix1.shape[0]-1)
    rowChecking = 0
    columnChecking = 0
    while (rowChecking < matrix1.shape[0] and columnChecking < matrix1.shape[1]):
        if matrix1[rowChecking, columnChecking] == 0:
            columnChecking += 1
            continue
        for row in range(rowChecking+1, matrix1.shape[0]):
            k =  matrix1[row, columnChecking] / matrix1[rowChecking, columnChecking]
            matrix1[row] = matrix1[row] - k*matrix1[rowChecking]
        correctOrderRows(matrix1, 0, matrix1.shape[0]-1)
        rowChecking += 1
        columnChecking += 1
    return matrix1

def det01(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return None
    matrix1 = gauss(matrix)
    det = 1
    for i in range(matrix1.shape[0]):
        det *= matrix1[i, i]
    return det
        
if __name__ == '__main__':
    matrix = numpy.random.randint(0, 101, size=(100, 100))
    print(matrix)
    # [[99 22 19 ... 61 93  7]
    #  [76 96 46 ...  1 69 92]
    #  [42 82 79 ... 96 42 69]
    #  ...
    #  [ 3 89 15 ... 16 84 21]
    #  [70 27 74 ...  4 14 19]
    #  [ 6 68  0 ... 34 69 88]]
  
    '''Viết một chương trình tính định thức của một ma trận (lưu dưới dạng một numpy array) bằng phương pháp khử Gauss.'''
    timeStart = time.time()
    print(det01(matrix))    # -1.460864200023446e+226
    time01 = time.time() - timeStart
    
    '''So sánh tốc độ của chương trình so với phương thức tính định thức có sẵn trong thư viện numpy.'''
    timeStart = time.time()
    print(numpy.linalg.det(matrix)) # -1.4608642000253283e+226
    time02 = time.time() - timeStart
    
    print("Without numpy:", time01) # Without numpy: 0.25367069244384766
    print("With numpy:", time02)    # With numpy: 0.01874542236328125
    # Tốc đọ khi sử dụng numpy nhanh hơn nhiều so với cách thủ công