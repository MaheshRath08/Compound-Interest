import math


# Create the function to evaluate Compound interest
def getCI(P, r, t):
    Amount = P*(math.pow((1 + r/100), t))
    CI = Amount - P
    return CI

#take the inputs
P = float(input("What is the principal Amount:\n"))
r = float(input("What is the rate of interest:\n"))
t = float(input("What is the time :\n"))

#call the function 
print(getCI(P, r, t))

