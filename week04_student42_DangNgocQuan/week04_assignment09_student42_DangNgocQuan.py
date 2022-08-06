def numberZerosEnding(n):
    count = 0
    tempNumber = 5
    while tempNumber <= n:
        count += n//tempNumber
        tempNumber *= 5
    return count

def lastDigitNewNumber(n):
    return factorial(n) // (10**numberZerosEnding(n)) % 10
        
def factorial(n):
    if n == 0:
        return 1
    return (n * factorial(n-1)) 

if __name__ == '__main__':
    '''a) Hỏi n! có bao nhiêu chữ số 0 ở tận cùng bên phải?'''
    print(numberZerosEnding(0))     # 0
    print(numberZerosEnding(5))     # 1
    print(numberZerosEnding(15))    # 3
    print(numberZerosEnding(25))    # 6
    print(numberZerosEnding(125))   # 31
    print(numberZerosEnding(625))   # 156
    
    '''b) Tạo một số mới bằng cách bỏ tất cả chữ số 0 ở tận cùng bên phải của n!.
    Hỏi chữ số tận cùng bên phải của số mới này bằng bao nhiêu?'''
    print(lastDigitNewNumber(0))        # 1
    print(lastDigitNewNumber(5))        # 2
    print(lastDigitNewNumber(15))       # 8
    print(lastDigitNewNumber(25))       # 4
    print(lastDigitNewNumber(125))      # 8
    print(lastDigitNewNumber(625))      # 6
    
    
    
    