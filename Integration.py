# 2019
# Integration
# Powered by LGleba
"""
We consider the integral using
the trapezoid method and the Boolean method
"""
from math import*
# Number Check Function
def check(x):
    S = str(x)
    if S == "":
        return
    kole = 0
    koltochka = 0
    kolminus = 0
    kolplus = 0
    flag = 1
    # I go over the substring
    for j in range(len(S)):
        if "0" <= S[j] <= "9":
            pass
        elif S[j] == "e":
            kole += 1
        elif S[j] == ".":
            koltochka += 1
        elif S[j] == "-":
            kolminus += 1
        elif S[j] == "+":
            kolplus += 1
        else:
            flag = 0
    if len(S) == 1 and "0" <= S <= "9":
        return float(S)
    if len(S) == 1 and (S == "-" or S == "+"):
        return
    if ((kolminus <= 1 or kolplus <= 1) and kole == 0 and koltochka <= 1) \
            and (S[0] == "-" or S[0] == "+"):
        return float(S)
    if kole > 1 or koltochka > 1 or kolminus > 2 or kolplus > 2:
        flag = 0
    if flag:
        indexe = -1
        indextochka = -1
        indexminus = 1e30
        indexplus = 1e30
        start = 0
        if S[0] == "-":
            start = 1
        elif S[0] == "+":
            start = 1
        elif S[0] == ".":
            pass
        for j in range(start, len(S), 1):
            if S[j] == "e":
                indexe = j
            elif S[j] == ".":
                indextochka = j
            elif S[j] == "-":
                indexminus = j
            elif S[j] == "+":
                indexplus = j
        if indextochka < indexe and (indexe + 1 == indexminus or\
                indexe + 1 == indexplus or (indexminus == 1e30 and\
                indexplus == 1e30)) and indexe > 0 and indexminus > indexe \
                and indexplus > indexe:
            flag = 1
        else:
            flag = 0
        if indexe == len(S) - 1:
            flag = 0
    if flag:
        return float(S)
    # Checking without e
    if kolminus <= 1 and kolplus <= 1 and kole == 0 and koltochka <= 1:
        koltochka = 0
        kolminus = 0
        kolwords = 0
        numberminus = 0
        chislo = ""
        for j in range(len(S)):
            if S[j] == "-":
                kolminus += 1
                numberminus = j
                chislo += S[j]
            elif S[j] == ".":
                koltochka += 1
                chislo += S[j]
            elif "0" <= S[j] <= "9":
                chislo += S[j]
            else:
                kolwords += 1
        if koltochka < 2 and kolwords == 0 and S[j] != "." and\
                S[j] != "-." and numberminus == 0:
            return float(S)
# Function f(x)
def f(x):
    return exp(x)
# Function F(x)
def perv(x):
    return exp(x)

# Trapezoid method function (basic) for the integral
def trap(a, b, n):
    h = (b - a) / n
    p = f(a)
    xi = a + h
    integ = 0
    for i in range(n):
        osnovanie = p + f(xi)
        integ += h * osnovanie/2
        p = f(xi)
        xi += h
    return integ

# Boolean function (main) for the integral
def Byll(a, b, n):
    if not n%4 == 0:
        return "NO"
    sh = (b-a)/n
    summa = 0
    for i in range(1,n//4+1):
        summa += (7*f(a+sh*(i*4-4))+32*f(a+sh*(i*4-3))+12*f(a+sh*(i*4-2))+
                  32*f(a+sh*(i*4-1))+7*f(a+sh*i*4))
    square = summa*2*sh/45
    return square

# Initial data
flag = 1

# Input control
a = input("Enter a: ")
if check(a) is None:
    flag = 0
else:
    a = float(a)
b = input("Enter b: ")
if check(b) is None:
    flag = 0
else:
    b = float(b)
n1 = input("Enter a split step n1: ")
if not n1.isdigit():
    flag = 0
else:
    n1 = int(n1)
    if n1 == 0:
        flag = 0
n2 = input("Enter a split step n2: ")
if not n2.isdigit():
    flag = 0
else:
    n2 = int(n2)
    if n2 == 0:
        flag = 0
# Data checking
if flag:
    #  Check a and b for more, less
    if a > b:
        a, b = b, a
    # We consider the integrals
    integ1 = trap(a, b, n1)
    integ2 = trap(a, b, n2)
    integ3 = Byll(a, b, n1)
    integ4 = Byll(a, b, n2)
    print("The integral is = {:<}".format(perv(b) - perv(a)))
    # Pseudo table
    print("┌────────────┬────────────┬────────────┐")
    print("│            │{:^12}│{:^12}│".format(n1, n2))
    print("├────────────┼────────────┼────────────┤")
    print("│{:12}│{:<12.4}│{:<12.4}│".format("M. trapezium", integ1, integ2))
    print("├────────────┼────────────┼────────────┤")
    print("│{:12}│{:<12.4}│{:<12.4}│".format("M. Boolean", integ3, integ4))
    print("└────────────┴────────────┴────────────┘")
    if integ3 == "NO" or integ4 == "NO":
        flag = 0
    if flag:
        if abs((integ1 + integ2)/2 - (perv(b) - perv(a))) >= abs((integ3 + integ4)/2 - (perv(b) - perv(a))):
            print("The Trapezoid Method is less accurate!")
            eps = input("Enter eps: ")
            flag = 1
            if check(eps) is None:
                flag = 0
            else:
                eps = float(eps)
            if flag:
                plosh = perv(b) - perv(a)
                nnew = 1
                flag = 1
                while abs(float(plosh) - float(trap(a, b, nnew))) > eps:
                    nnew += 1
                    if (nnew > 10000):
                        print("Looping, can't count, too long")
                        flag = 0
                        break
                if flag:
                   print("The integral is = {:<.4} for the {:} steps of the partitions".format(trap(a, b, nnew), nnew))
                   print("Accuracy {:.4}% or {:<12.4} ".format(abs(trap(a, b, nnew) - plosh)/plosh * 100, abs(trap(a, b, nnew) - plosh)))
            else:
                print("Invalid data entered")
        else:
            print("Boolean method is less accurate!")
            eps = input("Enter eps: ")
            flag = 1
            if check(eps) is None:
                flag = 0
            else:
                eps = float(eps)
            if flag:
                plosh = perv(b) - perv(a)
                nnew = 4
                flag = 1
                while abs(plosh - Byll(a, b, nnew)) > eps:
                    nnew += 4
                    if (nnew > 10000):
                        print("Break step > 10000, cannot count, too long")
                        flag = 0
                        break
                if flag:
                   print("The integral is = {:<.4} using the {:} splitting steps".format(Byll(a, b, nnew), nnew))
                   print("Accuracy {:.4}% or {:<12.4} ".format(abs(Byll(a, b, nnew) - plosh)/plosh * 100, abs(Byll(a, b, nnew) - plosh)))
            else:
                print("Invalid data entered")
    else:
        print("Not enough data to calculate the integral using eps")
else:
    print("Data Error!")
