import math


# Create the function to evaluate Compound interest
def getCI(P, r, n , t):
    Amount = P*(math.pow((1+(r/n)), n*t))
    CI = Amount - P
    return CI

#take the inputs
P = float(input("What is the principal Amount:\n"))
r = float(input("What is the rate of interest:\n"))
n = float(input("Number of times interest is compounded per unit:\n"))
t = float(input("What is the time :\n"))

#call the function 
print(getCI(P, r, n, t))

