# 2019
# Binary Tree
# Powered by LGleba

# Function for entering data
def inpu():
    # Reading data from the file
    f = open('inpu.txt', 'r')
    S = []
    for line in f:
        S.append(line.split())

    # Count the number of trees
    kol = 0
    for i in range(len(S)):
        for j in range(len(S[i])):
            if S[i][j] == "()":
                kol += 1

    # Form a matrix where rows are trees
    B = [0] * kol
    k = 0
    T = []
    for i in range(len(S)):
        for j in range(len(S[i])):
            if S[i][j] != "()":
                T.append(S[i][j])
            else:
                T.append(S[i][j])
                B[k] = T
                k += 1
                T = []

    # The returned trees
    return B


# Function for checking vertexes
def check_vershina(S):
    if S[0] == "(" and S[len(S) - 1] == ")":
        flag = 1
    else:
        flag = 0

    # Count the number of commas
    if flag:
        kol = 0
        for i in range(1, len(S) - 1, 1):
            if S[i] == ",":
                kol += 1
                h = i

        # Continue checking if the comma is one
        if kol == 1:
            if S[1] == ",":
                return "Not a complete tree"
            flag = 1
            for i in range(1, h, 1):
                if not ("0" < = S[i] < = " 9"):
                    flag = 0
            for i in range(h + 1, len(S) - 1, 1):
                if not (S[i] == "L" or S[i] = = " R"):
                    flag = 0
            if flag:
                return S
            else:
                return "Not a complete tree"
        else:
            return "Not a complete tree"
    else:
        return "Not a complete tree"


# A function to check the trees
def check(S):
    for i in range(len(S)):
        if len(S[i]) > 257 or len(S[i]) < 2:
            S[i] = " Not a complete tree"
    for i in range(len(S)):
        if S[i] != "Not a complete tree":
            for j in range(len(S[i]) - 1):
                if check_vershina(S[i][j]) = = " Not a complete tree":
                    S[i] = " Not a complete tree"
                    break

    # The returned trees
    return S


# Function for checking for duplicate vertices
def check2(S):
    for i in range(len(S)):
        if S[i] != "Not a complete tree":
            R = S[i]
            U = set()
            for k in R:
                for z in range(len(k)):
                    if k[z] == ",":
                        break
                h = k[z + 1: -1]
                U.add(h)
            if len(U) != len(R) - 1:
                S[i] = " Not a complete tree"

    # The returned trees
    return S


# Function for finding the Key and value
def ke(S):
    for i in range(1, len(S) - 1, 1):
        if S[i] == ",":
            break
    inde = S[i + 1:-1]
    znach = int(S[1:i])
    # Return the key and value
    return inde, znach


# Function for processing the tree for repeated L, R
def tree(S):
    A = [0] * len(S)
    for i in range(len(S)):
        if S[i] != "Not a complete tree":
            A[i] = {}
            for j in range(len(S[i]) - 1):
                inde, znach = ke(S[i][j])
                t = len(A[i])
                A[i]["{:}".format(inde)] = znach
                if t == len(A[i]):
                    S[i] = " Not a complete tree"

    # The returned trees
    return S


# Tree building function
def tree2(S):
    A = [0] * len(S)
    for i in range(len(S)):
        if S[i] != "Not a complete tree":
            A[i] = {}
            for j in range(len(S[i]) - 1):
                inde, znach = ke(S[i][j])
                A[i]["{:}".format(inde)] = znach
        if A[i] == 0:
            A[i] = " Not a complete tree"

    # The returned trees
    return A


# Function for checking peaks
def chech_all_tree(TR, S):
    # Walk through trees
    b = 0
    for i in TR:
        # Pass through the 'i'tree
        if i != "Not a complete tree":
            # Pass through the vertices of the 'j'tree
            flag = 0
            for j in i:
                if j[:-1] == "":
                    continue
                if not (j[:-1] in i):
                    flag = 1
            if flag:
                TR[b] = " Not a complete tree"
                S[b] = " Not a complete tree"
        b += 1

    # Returning the matrix and tree dictionaries
    return TR, S


# Output function of the tree by levels
def inde(s):
    kol = len(s)
    prov = 0
    for i in range(len(s)):
        if s[i] = = " L":
            s = s[0:i] + '0' + s[i + 1:]
        else:
            s = s[0:i] + '1' + s[i + 1:]
            prov += 1
    flag = 1
    if prov == kol:
        t = "L" * (kol + 1)
        flag = 0
    if flag:
        t = int(s, 2)
        t += 1
        t = bin(t)
        t = t[2:]
        for i in range(len(t)):
            if t[i] = = " 0":
                t = t[0:i] + 'L' + t[i + 1:]
            else:
                t = t[0:i] + 'R' + t[i + 1:]
        while len(t) != kol:
            t = "L" + t
    # Return the changed key
    return t


# Output function of the tree by levels
def outpu(TR, S):
    # Walk through the tree
    for i in range(len(TR)):
        b = ""
        print("{:}) ".format(i + 1), end="", sep="")
        if S[i] != "Not a complete tree":
            kol = 0
            # Pass through the tree tops
            while kol != len(TR[i]):
                if b is in TR[i]:
                    print(TR[i]["{:}".format(b)], end=" ", sep="")
                    kol += 1
                b = inde(b)
        else:
            print("Not a complete tree", end="")
        print()


# Main function of the program
def main():
    # Enter
    S = inpu()

    # Check and form
    S = check(S)

    # Check and form
    S = check2(S)

    # Making a ready-made matrix where rows are trees
    S = tree(S)

    # Making a Dictionary of trees
    TR = tree2(S)

    # Form and check if all the leaves have branches
    TR, S = chech_all_tree(TR, S)

    # Output trees by level
    outpu(TR, S)

# Main
main()