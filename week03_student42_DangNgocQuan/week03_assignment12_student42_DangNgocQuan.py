import math

def getMatrix(size):
    if size == 1:
        return [[1]]
    
    matrix = getMatrix(size-1)
    newRow = []
    tempNumber = (size-1)**2 + 1
    
    if size%2 == 0:
        for column in range(size):
            newRow.append(tempNumber)
            tempNumber += 1
        matrix.append(newRow)
        for row in range(size-2, -1, -1):
            matrix[row].append(tempNumber)
            tempNumber += 1
    else:
        for i in range(size):
            newRow.insert(0, tempNumber)
            tempNumber += 1
        matrix.insert(0, newRow)
        for row in range(1, size):
            matrix[row].insert(0, tempNumber)
            tempNumber += 1
    
    return matrix

def printAnswer(number):
    size = int(math.sqrt(number))
    if size**2 < number:
        size += 1
    matrix = getMatrix(size)
    
    for row in range(size):
        line = ""
        for column in range(size):
            value = matrix[row][column]
            if value <= number:
                line += "{0:>{1}}".format(value, len(str(number)) + 1)
            else:
                line += "{0:>{1}}".format(" ", len(str(number)) + 1)
        print(line)

if __name__ == '__main__':
    printAnswer(14)
    # 7  6  5
    # 8  1  4
    # 9  2  3 14
    # 10 11 12 13
    
    printAnswer(7)
    # 7 6 5
    # 1 4
    # 2 3
    
    printAnswer(42)
    #   42 41 40 39 38 37
    #   21 20 19 18 17 36
    #   22  7  6  5 16 35
    #   23  8  1  4 15 34
    #   24  9  2  3 14 33
    #   25 10 11 12 13 32
    #   26 27 28 29 30 31
    
    printAnswer(10)
    # 7  6  5
    # 8  1  4
    # 9  2  3
    # 10
    