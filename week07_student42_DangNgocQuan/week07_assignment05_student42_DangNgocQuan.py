import math

class Polynomial:
    def __init__(self, coefficientOfTerms):
        self.degree = len(coefficientOfTerms) - 1
        self.coefficientOfTerms = coefficientOfTerms
    
    def __repr__(self):
        text = ""
        for i in range(self.degree, -1, -1):
            if self.coefficientOfTerms[i] == 0:
                continue
            elif self.coefficientOfTerms[i] == -1:
                if i == 0:
                    text += "- " + str(-self.coefficientOfTerms[i]) + " "
                elif i == 1:
                    text += "- x "
                else:
                    text += "- x^" + str(i) + " "
            elif self.coefficientOfTerms[i] == 1:
                if i == 0:
                    text += "+ " + str(self.coefficientOfTerms[i]) + " "
                elif i == 1:
                    text += "+ x "
                else:
                    text += "+ x^" + str(i) + " "
            elif self.coefficientOfTerms[i] < 0:
                if i == 0:
                    text += "- " + str(-self.coefficientOfTerms[i]) + " "
                elif i == 1:
                    text += "- " + str(-self.coefficientOfTerms[i]) + "x "
                else:
                    text += "- " + str(-self.coefficientOfTerms[i]) + "x^" + str(i) + " "
            
            else:
                if i == 0:
                    text += "+ " + str(self.coefficientOfTerms[i]) + " "
                elif i == 1:
                    text += "+ " + str(self.coefficientOfTerms[i]) + "x "
                else:
                    text += "+ " + str(self.coefficientOfTerms[i]) + 'x^' + str(i) + " "
        if len(text) == 0:
            return text
        if text[0] == '-':
            return text
        return text[2:]
    
    def __add__(self, other):
        degree = max(self.degree, other.degree)
        coefficientOfTerms = []
        for i in range(degree + 1):
            coefficientOfTerms.append(0)
        for i in range(len(self.coefficientOfTerms)):
            coefficientOfTerms[i] += self.coefficientOfTerms[i]
        for i in range(len(other.coefficientOfTerms)):
            coefficientOfTerms[i] += other.coefficientOfTerms[i]
        return Polynomial(coefficientOfTerms)
    
    def __sub__(self, other):
        degree = max(self.degree, other.degree)
        coefficientOfTerms = []
        for i in range(degree + 1):
            coefficientOfTerms.append(0)
        for i in range(len(self.coefficientOfTerms)):
            coefficientOfTerms[i] += self.coefficientOfTerms[i]
        for i in range(len(other.coefficientOfTerms)):
            coefficientOfTerms[i] -= other.coefficientOfTerms[i]
        return Polynomial(coefficientOfTerms)
    
    def __neg__(self):
        degree = self.degree
        coefficientOfTerms = []
        for i in range(degree + 1):
            coefficientOfTerms.append(0)
        for i in range(len(self.coefficientOfTerms)):
            coefficientOfTerms[i] = -self.coefficientOfTerms[i]
        return Polynomial(coefficientOfTerms)
    
    def __mul__(self, other):
        degree = self.degree + other.degree
        coefficientOfTerms = []
        for i in range(degree + 1):
            coefficientOfTerms.append(0)
        for i in range(len(self.coefficientOfTerms)):
            for j in range(len(other.coefficientOfTerms)):
                coefficientOfTerms[i+j] += self.coefficientOfTerms[i] * other.coefficientOfTerms[j]
        return Polynomial(coefficientOfTerms)
    
    @classmethod
    def initializeFromString(cls, polynomialString):
        tempList = polynomialString.split(" ")
        
        marks = []
        for strig in tempList:
            if strig == '-' or strig == '+':
                marks.append(strig)
                tempList.remove(strig)
        
        degree = -1
        tempList = [strig.replace('^', '') for strig in tempList]
        exponent = tempList[0].split('x')[1]
        if exponent != '':
            degree = int(exponent)
        else:
            degree = 1
            
        coefficientOfTerms = []
        for i in range(degree+1):
            coefficientOfTerms.append(0)
        for strig in tempList:
            lst = strig.split('x')
            if len(lst) == 1:
                coefficientOfTerms[0] = int(lst[0])
            else:
                coefficient = lst[0]
                exponent = lst[1]
                if exponent != '':
                    exponent = int(exponent)
                else:
                    exponent = 1
                if coefficient == '':
                    coefficientOfTerms[exponent] = 1
                else:
                    coefficientOfTerms[exponent] = int(coefficient)
                    
        
        index = 0
        exponent = 0
        if len(marks) == len(tempList):
            exponent = degree
        else:
            exponent = degree - 1
        while (index < len(marks)):
            coefficient = coefficientOfTerms[exponent]
            if coefficient != 0:
                coefficientOfTerms[exponent] = int(marks[index] + str(coefficient))
                index += 1
            exponent -= 1
                
        return cls(coefficientOfTerms=coefficientOfTerms)
    

if __name__ == '__main__':
    polynomialA = Polynomial([1, 2, 3])
    print(polynomialA)      # 3x^2 + 2x + 1  
    polynomialB = Polynomial.initializeFromString('x^4 + 3x^2 - 5x + 1')
    print(polynomialB)      # x^4 + 3x^2 - 5x + 1
    polynomialC = polynomialA + polynomialB
    print(polynomialC)      # x^4 + 6x^2 - 3x + 2
    polynomialD = polynomialA - polynomialB
    print(polynomialD)      # - x^4 + 7x
    polynomialE = -polynomialA
    print(polynomialE)      # - 3x^2 - 2x - 1
    polynomialF = polynomialA * polynomialB
    print(polynomialF)      # 3x^6 + 2x^5 + 10x^4 - 9x^3 - 4x^2 - 3x + 1
