# 2019
# TextEditor
# Powered by LGleba
"""
Text editor
Need file "inpu.txt" with text
"""
# Function PlayGround
def playground(R):
    R = R + "*"
    if True:
        if True:
            p = 0
            chislo = 1
            flag = 0
            sposob = 1
            for g in range(len(R)):
                if g != len(R)-1:
                    if R[g] == "*" and R[g+1] == "*":
                        break
                    if R[g] == "*" and R[g+1] == "/":
                        break
                    if R[g] == "/" and R[g+1] == "*":
                        break
                    if R[g] == "/" and R[g+1] == "/":
                        break
                if R[g] == "*":
                    if not (check(R[p:g]) is None):
                        if sposob == 1:
                            chislo *= float(R[p:g])
                            p = g+1
                            flag = 1
                        if sposob == 2:
                            try:
                                chislo /= float(R[p:g])
                            except:
                                R = "'Calculation error'"
                                return R
                            p = g+1
                            flag = 1
                        sposob = 1
                    else:
                        break
                elif R[g] == "/":
                    if not (check(R[p:g]) is None):
                        if sposob == 1:
                            chislo *= float(R[p:g])
                            p = g+1
                            flag = 1
                        if sposob == 2:
                            try:
                                chislo /= float(R[p:g])
                            except:
                                R = "'Calculation error'"
                                return R

                            p = g+1
                            flag = 1
                        sposob = 2
                    else:
                        break
            if flag:
                R = chislo
            else:
                R = R[:-1]
    return R
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
def one(S):
    B = S
    kol = 0
    Bnew = [" "] * len(B)
    Te = [0] * len(B)
    Raz = [0] * len(B)
    for i in range(len(B)):
        Te[i] = [1] * (len(B[i]) - 1)
    for i in range(len(S)):
        for j in range(len(S[i])):
            Bnew[i] += S[i][j] + " "
        Bnew[i] = Bnew[i][1:-1]
    for i in range(len(Bnew)):
        if len(Bnew[i]) > kol:
            kol = len(Bnew[i])

    for i in range(len(B)):
        if kol != len(Bnew[i]):
            Raz[i] = kol - len(Bnew[i])

    for i in range(len(B)):
        sum = 0
        j = 0
        while sum != Raz[i]:
            if not(len(Te[i]) == 0):   
                Te[i][j % len(Te[i])] += 1
            sum += 1
            j += 1

    for i in range(len(B)):
        for j in range(len(B[i])):
            print("{:}".format(B[i][j]), sep="", end="")
            if j != len(B[i])-1:
                print(" " * Te[i][j], sep="", end="")
        print()
def two(S):
    for i in range(len(S)):
        for j in range(len(S[i])):
            if j != len(S[i]) - 1:
                print("{:} ".format(S[i][j]), end="")
            else:
                print("{:}".format(S[i][j]), end="")
        print()
def three(S):
    kol = 0
    Snew = [" "] * len(S)
    for i in range(len(S)):
        for j in range(len(S[i])):
            Snew[i] += S[i][j] + " "
        Snew[i] = Snew[i][1:-1]
    for i in range(len(Snew)):
        if len(Snew[i]) > kol:
            kol = len(Snew[i])
    for i in range(len(Snew)):
        while len(Snew[i]) != kol:
                Snew[i] = " " + Snew[i]
    for i in range(len(Snew)):
        for j in range(len(Snew[i])):
            print("{:}".format(Snew[i][j]), end="", sep="")
        print()

def four(S, word1, word2, outprint):
    for i in range(len(S)):
        for j in range(len(S[i])):
            if S[i][j] == word1:
                S[i][j] = word2
            elif S[i][j] == word1 + "," or S[i][j] == word1 + "." or\
                    S[i][j] == word1 + ":" or S[i][j] == word1 + ";" or\
                    S[i][j] == word1 + "!":
                q = S[i][j]
                q = q[-1:]
                S[i][j] = word2 + q
                if outprint == 1:
                    one(S)
                    return
                if outprint == 2:
                    two(S)
                    return
                if outprint == 3:
                    three(S)
                    return

    if outprint == 1:
        one(S)
        return
    if outprint == 2:
        two(S)
        return
    if outprint == 3:
        three(S)
        return
def five(S, word1, outprint):
    kol = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(len(S)):
            if flag:
                break
            flag = 0
            for j in range(len(S[i])):
                if flag:
                    break
                if S[i][j] == word1:
                    del S[i][j]
                    flag = 1
                elif S[i][j] == word1 + "," or S[i][j] == word1 + "." or\
                        S[i][j] == word1 + ":" or S[i][j] == word1 + ";" or\
                        S[i][j] == word1 + "!":
                    del S[i][j]
                    flag = 1

    if outprint == 1:
        one(S)
        return
    if outprint == 2:
        two(S)
        return
    if outprint == 3:
        three(S)
        return

def six(S, outprint):
    for i in range(len(S)):
        T = S[i]
        for j in range(len(T)):
            R = T[j]
            
            R = playground(R)
            
            T[j] = R
    
    if outprint == 1:
        one(S)
        return
    if outprint == 2:
        two(S)
        return
    if outprint == 3:
        three(S)
        return
def seven(S, outprint):
    kol = 0
    for i in range(len(S)):
        for j in range(len(S[i])):
            q = S[i][j]
            if q[-1:] == ".":
                kol += 1
    Pred = [" "] * kol
    p = 0
    for i in range(len(S)):
        for j in range(len(S[i])):
            q = S[i][j]
            Pred[p] = Pred[p] + q + " "
            if q[-1:] == ".":
                p += 1
    for i in range(len(Pred)):
        Pred[i] = Pred[i][1:-1]
        Pred[i] = Pred[i].split(" ")
    B = Pred

    flag = 1
    while flag:
        for i in range(0, len(B)-1, 1):
            flag = 0
            for j in range(i+1, len(B), 1):
                if len(B[i]) < len(B[j]):
                    B[i], B[j] = B[j], B[i]
                    flag = 1
    S = B
    if outprint == 1:
        one(S)
        return S
    if outprint == 2:
        two(S)
        return S
    if outprint == 3:
        three(S)
        return S


def inpu():
    f = open('inpu.txt', 'r')
    S = []
    for line in f:
        S.append(line.split())
    return S

def outpu(S):
    for i in range(len(S)):
        for j in range(len(S[i])):
            if j != len(S[i]) - 1:
                print("{:} ".format(S[i][j]), end="")
            else:
                print("{:}".format(S[i][j]), end="")
        print()

def main():
    print("Welcome to the text editor!")
    print()
    print("Your text:")
    S = inpu()
    outpu(S)
    print()
    print("Choose one of the following functions:")
    outprint = 2
    flag = 1
    while flag:
        print("1) Justify")
        print("2) Left justify")
        print("3) Right justify")
        print("4) Replacing the whole text of one word with another")
        print("5) Removing a given word from text")
        print("6) Replacing arithmetic expressions consisting of multiplication")
        print("and dividing by the result of their calculation")
        print("7) Print text sentences in descending order of the number of words in them")
        print("0) Exit the program")
        print()
        flag = input("Action selection: ")
        if flag.isdigit():
            flag = int(flag)
            if not (0 <= flag <= 7):
                print("Input Error")
                continue
        else:
            print("Input Error")
            continue
        if flag == 1:
            print("New text:")
            outprint = 1
            one(S)
            print()
            continue
        if flag == 2:
            print("New text:")
            outprint = 2
            two(S)
            print()
            continue
        if flag == 3:
            print("New text:")
            outprint = 3
            three(S)
            print()
            continue
        if flag == 4:
            word1 = input("Enter the word you want to replace: ")
            word2 = input("Enter the word you want to replace with: ")
            print("New text:")
            four(S, word1, word2, outprint)
            print()
            continue
        if flag == 5:
            word1 = input("Enter the word you want to delete: ")
            print("New text:")
            five(S, word1, outprint)
            print()
            continue
        if flag == 6:
            print("New text:")
            six(S, outprint)
            print()
            continue
        if flag == 7:
            print("New text:")
            S = seven(S, outprint)
            print()
            continue
main()
