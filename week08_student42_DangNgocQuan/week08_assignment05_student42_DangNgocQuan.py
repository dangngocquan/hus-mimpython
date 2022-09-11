
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b) 

class Fraction:
    def __init__(self, numerator = 1, denominator = 1):
        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)
        
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __add__(self, anotherFract):
        return Fraction(numerator=self.numerator * anotherFract.denominator + self.denominator * anotherFract.numerator,
                        denominator=self.denominator * anotherFract.denominator)
        
    def __radd__(self, another):
        return self.__add__(another)
    
    def __eq__(self, anotherFract):
        return self.numerator * anotherFract.denominator == self.denominator * anotherFract.numerator

def printSolutionAndSave():
    print(f"A={missingDigits[0]} B={missingDigits[1]} C={missingDigits[2]} " +
          f"D={missingDigits[3]} E={missingDigits[4]} F={missingDigits[5]} " + 
          f"G={missingDigits[6]} H={missingDigits[7]} I={missingDigits[8]}")
    with open('./week08_student42_DangNgocQuan/additionalFolder/assignment05/answer.txt', 'a') as file:
        file.write(f"A={missingDigits[0]} B={missingDigits[1]} C={missingDigits[2]} " +
          f"D={missingDigits[3]} E={missingDigits[4]} F={missingDigits[5]} " + 
          f"G={missingDigits[6]} H={missingDigits[7]} I={missingDigits[8]}\n")
    file.close()
    
    
def solve(indexFinding: int):
    global countAns
    global isUsed
    global missingDigits
    if indexFinding >= 9:
        leftExpression = Fraction(missingDigits[0]) + Fraction(missingDigits[1], missingDigits[2])
        leftExpression += Fraction(missingDigits[3]) + Fraction(missingDigits[4], missingDigits[5])
        rightExpression = Fraction(missingDigits[6]) + Fraction(missingDigits[7], missingDigits[8])
        if leftExpression == rightExpression:
            printSolutionAndSave()
            countAns += 1
    else:
        for value in range(1, 10):
            if isUsed[value] == False:
                missingDigits[indexFinding] = value
                isUsed[value] = True
                solve(indexFinding+1)
                missingDigits[indexFinding] = 0
                isUsed[value] = False
                
    

if __name__ == '__main__':
    countAns = 0
    missingDigits = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    isUsed = [False, False, False, False, False, False, False, False, False, False]
    solve(0)
    print(f"Count answer: {countAns}")
    with open('./week08_student42_DangNgocQuan/additionalFolder/assignment05/answer.txt', 'a') as file:
        file.write(f"Count answer: {countAns}\n")
    file.close()
    
    