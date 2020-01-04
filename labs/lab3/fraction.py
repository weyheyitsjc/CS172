class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self,a,b):
        self.num = a
        self.den = b
        self.simplify()
    #Print Fraction as a String
    def __str__(self):
        if self.den==1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)
    #Get the Numerator
    def getNum(self):
        return self.num
    #Get the Denominator
    def getDen(self):
        return self.den
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.num/self.den
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.num,self.den)
        self.num = self.num // x
        self.den = self.den // x
    #Find the GCD of a and b
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a % b)
    #Complete these methods in lab
    def __add__(self,other):
        a = self.num
        x = other.num
        b = self.den
        y = other.den
        
        fractionNum = (a * y) + (x * b)
        fractionDen = b * y
        
        return Fraction(fractionNum, fractionDen)
    def __sub__(self,other):
        x = other.num * -1
        a = self.num
        b = self.den
        y = other.den
        
        fractionNum = (a * y) + (x * b)
        fractionDen = b * y
        
        return Fraction(fractionNum, fractionDen)
    def __mul__(self,other):
        fractionNum = self.num * other.num
        fractionDen = self.den * other.den
        fraction = Fraction(fractionNum, fractionDen)
        return fraction
    def __truediv__(self,other):
        fractionNum = self.num * other.den
        fractionDen = self.den * other.num
        fraction = Fraction(fractionNum, fractionDen)
        return fraction
    def __pow__(self,exp):
        if exp < 0:
            exp = exp * -1
            fractionNum = (self.den) ** exp
            fractionDen = (self.num) ** exp
            fraction = Fraction(fractionNum, fractionDen)
            return fraction
        elif exp == 0:
            return Fraction(1, 1)
        elif exp > 0:
            fractionNum1 = self.num
            fractionDen1 = self.den
            fractionNum2 = (self.num) ** (exp - 1)
            fractionDen2 = (self.den) ** (exp - 1)
            fractionNum = fractionNum1 * fractionNum2
            fractionDen = fractionDen1 * fractionDen2
            fraction = Fraction(fractionNum, fractionDen)
            return fraction
#if __name__ == "__main__":
    #a = Fraction(5, 6)
    #b = Fraction(1, 6)
    #print(a.__sub__(b))
