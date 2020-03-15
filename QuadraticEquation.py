# 2019
# QuadraticEquation
# Powered by LGleba
"""
Meaning:
    Using the given coefficients,
    find the roots of the quadratic equation.
Condition:
    a*(x^2) + b*(x) + c = 0 
"""
# Import the root function from the Math module
from math import sqrt

print(" ________________________________________________________________")
print("|\t\t\tTask")
print("|Using the given coefficients, find the roots of the quadratic equation.")
print("|________________________________________________________________")
# Entering Odds
a, b, c = map(float, input("|Enter the odds through a space: ").split())
print("|________________________________________________________________")

# Check the coefficient a
if (a == 0):
    # Check the coefficient b
    if (b == 0):
        # Check the coefficient c
        if (c == 0):
            # Response output
            print("|X - any") 
        else:
            # Response output
            print("|There is no decision") 
    else:
        # Root calculation
        x = -c/b
        # Response output
        print("|Answer: {0:.4}".format(x)) 
else:
    # Discriminant Calculation
    D = b*b-4*a*c 
    if (D >= 0):
        # Computing the root of the discriminant
        D = sqrt(D)
        # Calculation of 1 root
        x1 = (-b+D)/(2*a)
        # Calculation of 2 roots
        x2 = (-b-D)/(2*a) 
        if (x1 == x2):
            # Response output
            print("|Answer: {0:.4}".format(x1)) 
        else:
            # Response output		
            print("|Answer: x1 = {0:.4}, x2 = {1:.4}".format(x1,x2))
    else:
        # Response output
        print("|X - invalid number") 
print("|________________________________________________________________")
input("\t\tTo close the program, press 'Enter'")
