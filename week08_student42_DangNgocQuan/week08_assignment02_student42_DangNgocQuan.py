import random
import time
import numpy as np

def subRows(k1: float, firstRow: list, k2: float, secondRow: list) -> list:
    assert len(firstRow) == len(secondRow)
    return [k1 * firstRow[i] - k2 * secondRow[i] for i in range(len(firstRow))]

def solveLinearEquationsWithoutNumpy(A: list, B: list) -> list:
    assert len(A) == len(A[0]) and len(A) == len(B)
    A1 = [row.copy() for row in A]
    B1 = B.copy()
    
    for row in range(len(A1)):
        if A1[row][row] == 0:
            indexRow = -1
            for index in range(row+1, len(A1)):
                if A1[index][row] != 0:
                    indexRow = index
                    break
            if indexRow == -1:
                return None
            tempRow = A1[row]
            A1[row] = A1[indexRow]
            A1[indexRow] = tempRow
            temp = B[row]
            B1[row] = B1[indexRow]
            B1[indexRow] = temp
        k = A1[row][row]
        B1[row] /= k
        for index in range(len(A1[row])):
            A1[row][index] /= k
        for index in range(row+1, len(A1)):
            B1[index] = B1[index] - A1[index][row] * B1[row]
            A1[index] = subRows(1, A1[index], A1[index][row], A1[row])

    
    for row in range(len(A1) - 1, -1, -1):
        for indexRow in range(row):
            B1[indexRow] = B1[indexRow] - A1[indexRow][row] * B1[row]
            A1[indexRow] = subRows(1, A1[indexRow], A1[indexRow][row], A1[row])
    return B1

def solveLinearEquationsWithNumpy(A: list, B: list) -> list:
    return np.linalg.solve(A, B)

if __name__ == '__main__':
    A = [[random.randint(0, 100) for i in range(50)] for j in range(50)]
    B = [random.randint(0, 100) for i in range(50)]
    timeStart = time.time()
    print(solveLinearEquationsWithoutNumpy(A, B))
    time1 = time.time() - timeStart
    timeStart = time.time()
    print(solveLinearEquationsWithNumpy(A, B))
    time2 = time.time() - timeStart
    print(f"Runtime without numpy: {time1}")    # Runtime without numpy: 0.013975858688354492
    print(f"Runtime with numpy: {time2}")   # Runtime with numpy: 0.004247903823852539
    # ==> Dùng thư viện numpy thì tốc độ nhanh hơn so với tự viết hàm thủ công