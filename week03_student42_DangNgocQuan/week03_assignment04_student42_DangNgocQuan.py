import numpy as np
import sympy

def fibonacciUsingNumpy(n):
    if n == 0:
        return 0
    matrix = np.array([[1, 1], [1, 0]])
    f = np.copy(matrix)
    for i in range(n-1):
       f = np.dot(f, matrix)
    return f[0, 1]

def fibonacciUsingSympy(n):
    return sympy.fibonacci(n, 1)

if __name__ == '__main__':
    # Cách 1: Dùng numpy
    print(fibonacciUsingNumpy(6))       # 8
    print(fibonacciUsingNumpy(10))      # 55
    print(fibonacciUsingNumpy(15))      # 610
    
    # Cách 2: Dùng sympy
    print(fibonacciUsingSympy(6))       # 8
    print(fibonacciUsingSympy(10))      # 55
    print(fibonacciUsingSympy(15))      # 610