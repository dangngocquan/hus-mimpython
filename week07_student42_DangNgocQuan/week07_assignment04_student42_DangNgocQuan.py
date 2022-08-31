import math

def gcd(num1, num2):
    if (num2 == 0):
        return num1
    return gcd(num2, num1 % num2)

class Fraction:
    def __init__(self, numerator=1, denominator=2):
        assert denominator != 0
        if (denominator < 0):
            self.numerator = -numerator
            self.denominator = -denominator
        else:
            self.numerator = numerator
            self.denominator = denominator
        
    def __repr__(self):
        return f"Fraction({self.numerator},{self.denominator})"
    
    def reducedFraction(self):
        k = gcd(num1=math.fabs(self.numerator), num2=math.fabs(self.denominator))
        self.numerator = int(self.numerator // k)
        self.denominator = int(self.denominator // k)
        
    def __add__(self, anotherFraction):
        fraction = Fraction(numerator=self.numerator * anotherFraction.denominator + self.denominator * anotherFraction.numerator,
                            denominator=self.denominator * anotherFraction.denominator)
        fraction.reducedFraction()
        return fraction
    
    def __sub__(self, anotherFraction):
        fraction = Fraction(numerator=self.numerator * anotherFraction.denominator - self.denominator * anotherFraction.numerator,
                            denominator=self.denominator * anotherFraction.denominator)
        fraction.reducedFraction()
        return fraction
    
    def __mul__(self, anotherFraction):
        fraction = Fraction(numerator=self.numerator * anotherFraction.numerator,
                            denominator=self.denominator * anotherFraction.denominator)
        fraction.reducedFraction()
        return fraction
        
    def __truediv__(self, anotherFraction):
        fraction = Fraction(numerator=self.numerator * anotherFraction.denominator,
                            denominator=self.denominator * anotherFraction.numerator)
        fraction.reducedFraction()
        return fraction
    
    def __ge__(self, anotherFraction):
        return self.numerator * anotherFraction.denominator >= self.denominator * anotherFraction.numerator
    
    @classmethod
    def initializeFromFloat(cls, value=float):
        numerator = value
        denominator = 1
        while (numerator != int(numerator)):
            numerator *= 10
            denominator *= 10
        numerator = int(numerator)
        denominator = int(denominator)
        fraction = cls(numerator=numerator, denominator=denominator)
        fraction.reducedFraction()
        return fraction
        
        
if __name__ == '__main__':
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction.initializeFromFloat(0.42)
    print(fraction1)    # Fraction(1,2)
    print(fraction2)    # Fraction(21,50)
    print(fraction1 + fraction2)    # Fraction(23,25)
    print(fraction1 - fraction2)    # Fraction(2,25)
    print(fraction1 * fraction2)    # Fraction(21,100)
    print(fraction1 / fraction2)    # Fraction(25,21)
    print(fraction1 >= fraction2)   # True
    
    
    '''Câu hỏi nâng cao. Sau khi đã cài đặt __add__, liệu có thể sử dụng cách viết:
    totalValue = sum([fractionA, fractionB, fractionC])
    được hay không?
    - Không
    '''
    print(sum[fraction1, fraction1, fraction2])
    # TypeError: 'builtin_function_or_method' object is not subscriptable
    