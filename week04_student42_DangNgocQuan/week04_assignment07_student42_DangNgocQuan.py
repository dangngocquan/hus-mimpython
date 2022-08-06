import math

class Polynomial:
    def __init__(self, degree, coefficientOfTerms):
        self.degree = degree
        self.coefficients = coefficientOfTerms
    
    def __repr__(self):
        text = ""
        for i in range(self.degree, -1, -1):
            if self.coefficients[i] == 0:
                continue
            if self.coefficients[i] < 0:
                text += " + (" + str(self.coefficients[i]) + ')*x^' + str(i)
            else:
                text += " + " + str(self.coefficients[i]) + '*x^' + str(i)
        if len(text) == 0:
            return text
        return text[3:]
    
    def __add__(self, other):
        degree = max(self.degree, other.degree)
        coefficients = []
        for i in range(degree + 1):
            coefficients.append(0)
        for i in range(len(self.coefficients)):
            coefficients[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            coefficients[i] += other.coefficients[i]
        return Polynomial(degree, coefficients)
    
    def __sub__(self, other):
        degree = max(self.degree, other.degree)
        coefficients = []
        for i in range(degree + 1):
            coefficients.append(0)
        for i in range(len(self.coefficients)):
            coefficients[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            coefficients[i] -= other.coefficients[i]
        return Polynomial(degree, coefficients)
    
    def __neg__(self):
        degree = self.degree
        coefficients = []
        for i in range(degree + 1):
            coefficients.append(0)
        for i in range(len(self.coefficients)):
            coefficients[i] = -self.coefficients[i]
        return Polynomial(degree, coefficients)
    
    def __mul__(self, other):
        degree = self.degree + other.degree
        coefficients = []
        for i in range(degree + 1):
            coefficients.append(0)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                coefficients[i+j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(degree, coefficients)
    

if __name__ == '__main__':
    polynomialA = Polynomial(2, [2, 3, 5])
    print(polynomialA)      # 5*x^2 + 3*x^1 + 2*x^0
    polynomialB = Polynomial(1, [-2, -3])
    print(polynomialB)      # (-3)*x^1 + (-2)*x^0
    polynomialC = polynomialA + polynomialB
    print(polynomialC)      # 5*x^2
    polynomialD = polynomialA - polynomialB
    print(polynomialD)      # 5*x^2 + 6*x^1 + 4*x^0
    polynomialE = -polynomialA
    print(polynomialE)      # (-5)*x^2 + (-3)*x^1 + (-2)*x^0
    polynomialF = polynomialA * polynomialB
    print(polynomialF)      # (-15)*x^3 + (-19)*x^2 + (-12)*x^1 + (-4)*x^0