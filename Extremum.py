# 2019
# Extremum
# Powered by LGleba
"""
For the entered array, determine the number of extrema
"""
print("'For the entered array, determine the number of extrema'")
print()
A = list(input("Enter the elements of the array with a space: ").split())
n = len(A)
B = []
kol = 0
# I go over the entire line
for i in range(n):
    S = A[i]
    kole = 0
    koltochka = 0
    kolminus = 0
    kolplus = 0
    flag = 1
    #  I go over the substring
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
    if len(S) == 1:
        S += " "
    if S[1] == "-" or S[1] == "+":
        continue
    if ((kolminus <= 1 or kolplus <= 1) and kole == 0 and koltochka <= 1) \
            and (S[0] == "-" or S[0] == "+"):
        B.append(float(S))
        continue
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
        if indextochka < indexe and (indexe + 1 == indexminus or indexe + 1 == indexplus or\
                (indexminus == 1e30 and indexplus == 1e30)) and\
                indexe > 0 and indexminus > indexe and indexplus > indexe:
            flag = 1
        else:
            flag = 0
        if indexe == len(S) - 1:
            flag = 0
    if flag:
        B.append(float(S))
    # Checking without e
    if kolminus <= 1 and kolplus <= 1 and kole == 0 and koltochka <= 1:
        koltochka = 0
        kolminus = 0
        kolwords = 0
        numberminus = 0
        chislo = ""
        for j in range(len(A[i])):
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
        if koltochka < 2 and kolwords == 0 and S[j] != "." and S[j] != "-." and numberminus == 0:
            B.append(float(chislo))
n = len(B)
print()
print("Array initial:\n{}".format(B))
print()
if len(B) == 2 and B[0] != B[1]:
    kol = 1
for i in range(1, n-1, 1):
    if B[i-1] < B[i] > B[i+1] or B[i-1] > B[i] < B[i+1] or\
            B[i-1] == B[i] < B[i+1] or B[i-1] == B[i] > B[i+1] or\
            B[i-1] < B[i] == B[i+1] or B[i-1] > B[i] == B[i+1]:
        kol += 1
print("Number of extreme points = {:<12}".format(kol))
