# 2019
# RefinementRoots
# Powered by LGleba
"""
Refinement of roots by Newton's method (tangents)
"""
from math import cos, sin
# Function function
def f(x):
    y = x*x - 4
    return y

# The function is derived from function
def dfdx(x):
    y = 2*x
    return y

# Newton method
def Newton(x, eps):
    # Function value
    f_value = f(x)

    # Number of iterations
    iteration_counter = 0

    # Consider the roots
    while abs (f_value) > eps and iteration_counter < 1000:
        try:
            x = x - f_value/dfdx(x)
        except:
            break
        f_value = f(x)
        iteration_counter += 1

    # Checking for errors
    if abs (f_value) > eps:
        iteration_counter = -1

    # Return the root and the number of iterations
    return x, iteration_counter

# main function
def main():
    A = []
    print ("Welcome!\n")
    print ("Find the roots of the function.")

    # Flag
    flag = 1

    # Check a fool
    while flag:
        try:
            start = float(input ("Enter the starting point: "))
            stop = float(input ("Enter an endpoint: "))
            shag = float(input ("Enter step: "))
            eps = float(input ("Enter eps: "))
            flag = 0
        except:
            print("\nerror!\n")

    # The number of the iteration
    kol = 1

    # Number of iterations
    if (abs(stop - start)/shag) != (abs (stop-start)/ / shag):
        r = abs(stop - start) // shag + 1
    else:
        r = abs(stop - start) // shag

    print()
    print("┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐")
    print("│{:^13}│{:^13}│{:^13}│{:^13}│{:^13}│{:^13}│".format("Number of inter.", "Interval", " Value. root", " Meaning. function", "number eteraz", "error Code"))

    # Building a table
    i = start
    flag = 0
    flag2 = 0
    for k in range(int(r)):
        try:
            kod = " NO"
            x, iters = Newton(i, eps)
            x = round(x, 1)
            if iters == -1:
                kod = " > > eps"
            if ((i <= x < i+shag) and (kod != "An error > eps") and (x not in A)):
                if kol != r:
                    print("├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤")
                    print("│{:^13}│{:<5.4} - {:>5.4}│{:>13.4}│{:>13.4 e}│{:13}│{:^13}│".format(kol, i, i + shag, x, f(x), I), kod))
                    flag2 = 1
                    A. append(x)
                else:
                    print("├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤")
                    print("│{:^13}│{:<5.4} - {:>5.4}│{:>13.4}│{:>13.4 e}│{:13}│{:^13}│".format(kol, i, stop, x, f(x), I), kod))
                    flag2 = 1
                    A. append(x)

            flag = 1
        except:
            pass
        kol += 1
        i += shag
        if kol == r:
            shag += 0.001
    if flag2 == 0:
        print("├─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┤")
        print("│{:^83}│".format ("no Records!"))
        print("└───────────────────────────────────────────────────────────────────────────────────┘")
    elif flag:
        print("└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘")
# Main
main()
# 2019
# Laboratory 10.2
# Powered by LGleba
"""
Refinement of roots by Newton's method (tangents)
"""
from mathematics import, because, sin
# Functions Function
def f(x):
    y = x*x-4
    return g

# The function is derived from function
def dfdx(x):
    y = 2*x
    return g

# Newton method
def Newton(x, eps):
    # Function value
    f_value = F(x)

    # Number Of Iterations
    iteration_counter = 0

    # Consider the roots
    while abs (f_value) > eps and iteration_counter < 1000:
        try:
            x = x-f_value/dfdx(x)
        except:
            break
        f_value = F(x)
        iteration_counter += 1

    # Checking for errors
    if abs (f_value) > eps:
        iteration_counter = -1

     Return the number of iterations root and #
    return x, iteration_counter

# main function
Def home():
    La = []
    seal ("Welcome!\North")
    print ("Find the roots of the function.")

    # Flag
    flag = 1

    # Check a fool
    while the flag:
        try:
            start = float (input ("Enter the starting point: "))
            stop = float (input ("Enter an endpoint: "))
            shag = float (input ("Enter step: "))
            eps = float (input ("Enter EPS: "))
            flag = 0
        except:
            print ("\nerror!\North")

    # The number of the iteration
    Number = 1

    # Number of iterations
    if (abs (stop-start) / shag)!= (abs (stop-start) / / shag):
        r = abs (stop-start) / / shag + 1
    still:
        r = abs (stop-start) / / shag

    print()
    print("┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐")
    print("│{:^13}│{:^13}│{:^13}│{:^13}│{:^13}│{:^13}│".format ("inter Number.", "Interval", " Value. root", " meaning. function", "number eteraz"," error Code"))

    # Building a table
    I = beginning
    flag = 0
    flag2 = 0
    for k in the range (int(r)):
        try:
            code = " no"
            x, iters = Newton (i, eps)
            x = round(x, 1)
            if iters = = -1:
                kod = " > > EPS"
            if ((i <= x < i+shag) and (kod != "X > EPS") and (X not in A)):
                if the stake != p:
                    print("├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤")
                    print("│{:^13}│{:<5.4} - {:>5.4}│{:>13.4}│{:>13.4 e}│{:13}│{:^13}│".format (Qty, I , I + step, X, f (x), iters code))
                    flag2 = 1
                    A. add(x)
                still:
                    print("├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤")
                    print("│{:^13}│{:<5.4} - {:>5.4}│{:>13.4}│{:>13.4 e}│{:13}│{:^13}│".format (count, I, stop, X, f (x), iters code))
                    flag2 = 1
                    A. add(x)

            flag = 1
        except:
            pass
        Number += 1
        I + = step
        if kol = = r:
            step += 0.001
    if flag2 = = 0:
        print("├─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┤")
        print("│{:^83}│".format ("no Records!"))
        print("└───────────────────────────────────────────────────────────────────────────────────┘")
    elif flag:
        print("└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘")
# Main
main()
