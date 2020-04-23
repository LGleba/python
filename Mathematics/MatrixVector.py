# 2019
# MatrixVector
# Powered by LGleba
"""
Calculate the sum of the series t = E ((a ^ (2n + 1)) / (2n + 1)) with accuracy EPS.
Next, in the matrix Z (15.10), determine the elements that are large values of the calculated
sum, row t (view the matrix to lead in rows) and remember these elements
in a one-dimensional array X. Swap in the array X the first element with
maximum. Print the sum of the series, the matrix Z in the form of a matrix, and the vector X
"""
# Import factorial function from math module
from math import factorial

# Number check function
def check(x):
    S = str(x)
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
        if koltochka < 2 and kolwords == 0 and S[j] != "." and S[j] != "-." \
                and numberminus == 0:
            return float(S)
print ("Calculate the sum of the series t = E ((a ^ (2n + 1)) / (2n + 1)) with an accuracy of EPS. \ n" +
"Next, in the matrix Z (15.10), determine the elements that are large values of the calculated \ n" +
"sums, row t (scan the matrix in rows) and remember these elements \ n" +
"in a one-dimensional array X. Swap in the array X the first element with \ n" +
"maximum. Print the sum of the series, the matrix Z in the form of a matrix, and the vector X \ n")

flag = 1
a = input ("Enter a (argument for the sum of the series): ")
eps = input ("Enter eps (precision): ")
if check(a) is None or check(eps) is None:
    flag = 0
else:
    a = float(a)
    eps = float(eps)
if flag:
    rows = 15
    columns = 10
    Z = [0]*rows
    print("Enter a 15x10 matrix as a matrix")
    # Input matrix
    for i in range(rows):
        Z[i] = list(input("{:3}| ".format(i+1)).split())
        if len(Z[i]) != columns:
            flag = 0
            break
        for r in range(columns):
            if check(Z[i][r]) is None:
                flag = 0
                break
            else:
                Z[i][r] = float(Z[i][r])
    if flag:
        t = a
        n = 1
        sum = 0
        op = 0
        max = 1e-100
        X = []
        print()
        # We consider the sum of the series
        while abs(t) > eps:
            print("{:>3}) {:12.4}".format(n, t))
            sum += t
            t = a**(2*n + 1)/factorial(2*n+1)
            n += 1
        for i in range(rows):
            for j in range(columns):
                if Z[i][j] > sum:
                    X.append(Z[i][j])
                    if Z[i][j] > max:
                        max = Z[i][j]
                        indexmax = op
                    op += 1
        print()
        print("The sum of the series is: {:<12.4}".format(sum))
        print()
        print("Array of X before replacement: ")
        print(X)
        print()
        # Swap the first element with the maximum
        X[indexmax], X[0] = X[0], X[indexmax]
        print("Mac OS X after replacement: ")
        print(X)
        print()
        print("Matrix Z")
        for i in range(rows):
            for j in range(columns):
                print("{:<12.4}".format(Z[i][j]), end=" ")
            print()
    else:
        print("Data Error!")
else:
    print("Data Error!")
