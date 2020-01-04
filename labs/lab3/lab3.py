from fraction import Fraction

def harmonic_series(n):
    total = Fraction(0,1)
    for x in range(1, (n + 1)):
        total += Fraction(1,x) 
    return total

def Two(n):
    k = 0
    total = Fraction(k,1)
    for x in range(k, n+1):
        total += Fraction(1,2)**x
    return total

def Zero(n):
    k = 0
    total = Fraction(k,1)
    for x in range(k, n + 1):
        i = (Fraction(1,2)**x)
        total += i
    return Fraction(2, 1) - total
    
def Riemann(n,b):
    total = Fraction(0,1)
    for x in range(1, n+1):
        i = Fraction(1,x) ** b
        total = total + i
    return total
    

if __name__ == "__main__":
    print("Welcome to Fun with Fractions!")
    iterations = input("Enter Number of iterations (integer > 0):\n")
    x = 0
    while x == 0:
        try:
            iterations = int(iterations)
            if iterations > 0:
                x = 1
            else:
                iterations = input("Enter Number of iterations (integer > 0):\n")
        except:
            iterations = input("Enter Number of iterations (integer > 0):\n")
            
    print("H(" + str(iterations) + ")" + '=' + str(harmonic_series(iterations)))
    print("H(" + str(iterations) + ")" + '~=' + str(((harmonic_series(iterations)).getNum())/(harmonic_series(iterations)).getDen()))
    print("T(" + str(iterations) + ")" + '=' + str(Two(iterations)))
    print("T(" + str(iterations) + ")" + '~=' + str(((Two(iterations)).getNum())/(Two(iterations)).getDen()))
    print("Z(" + str(iterations) + ")" + '=' + str(Zero(iterations)))
    print("Z(" + str(iterations) + ")" + '~=' + str(((Zero(iterations)).getNum())/(Zero(iterations)).getDen()))
    
    for b in range(2,9):
        print("R(" + str(iterations) + "," + (str(b)) + ")" + '=' + str(Riemann(iterations, b)))
        print("R(" + str(iterations) + "," + (str(b)) + ")" + '~=' + str(((Riemann(iterations,b)).getNum())/(Riemann(iterations,b)).getDen()))