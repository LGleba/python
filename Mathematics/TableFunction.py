# 2019
# TableFunction
# Powered by LGleba
"""
Meaning:
    Create a table with function values
"""
# Import
from math import sin
# Flag
flag = True
# Mines and Maxes
c_min, y_min, m_min = 1e100, 1e100, 1e100
c_max, y_max, m_max = -1e100, -1e100, -1e100
print ("Functions")
print("1) C = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a**2 - 5*a + 1")
print("2) Y = sin(x) * x")
print("3) M = x^2 -25")

while flag:
    # Initial value
    start = float(input("Enter the initial value of a: "))
    # Final value
    finish = float(input("Enter the final value of a: "))
    # Step
    shag = float(input("Enter step: "))
    # Check for ascending or descending
    if (start < finish and shag > 0.0) or (start > finish and shag < 0.0) \
            or (start == finish):
        if shag != 0:
            print(chr(9484) + chr(9472) * 12 + chr(9516) + chr(9472) * 12
                  + chr(9488))
            print(chr(9474) + "{:^12}".format("a") + chr(9474) +
                  "{:^12}".format("C") + chr(9474))
            print(chr(9500) + chr(9472) * 12 + chr(9532) + chr(9472) * 12
                  + chr(9508))
            # Number of operations
            n = int((finish - start)/shag + 1)
            a = start
            flag = 1
            # Function 1
            for i in range(n):
                if i + 1 == n:
                    flag = 0
                c = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a**2 - 5*a + 1
                if c < c_min:
                    c_min = c
                if c > c_max:
                    c_max = c
                print(chr(9474) + "{:<12.5}".format(a) + chr(9474) +
                      "{:<12.5}".format(c) + chr(9474))
                # Check for last iteration
                if flag:
                    print(chr(9500) + chr(9472)*12 + chr(9532) + chr(9472)*12
                          + chr(9508))
                else:
                    print(chr(9492) + chr(9472)*12 + chr(9524) + chr(9472)*12
                          + chr(9496))
                a += shag
            print()
            print(chr(9484) + chr(9472) * 12 + chr(9516) + chr(9472) * 12
                  + chr(9488))
            print(chr(9474) + "{:^12}".format("x") + chr(9474) +
                  "{:^12}".format("Y") + chr(9474))
            print(chr(9500) + chr(9472) * 12 + chr(9532) + chr(9472) * 12
                  + chr(9508))
            # Function 2
            x = start
            flag = 1
            for i in range(n):
                if i + 1 == n:
                    flag = 0
                y = sin(x) * x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y
                print(chr(9474) + "{:<12.5}".format(x) + chr(9474) +
                      "{:<12.5}".format(y) + chr(9474))
                # Check for last iteration
                if flag:
                    print(chr(9500) + chr(9472)*12 + chr(9532) + chr(9472)*12
                          + chr(9508))
                else:
                    print(chr(9492) + chr(9472)*12 + chr(9524) + chr(9472)*12
                          + chr(9496))
                x += shag
            print()
            print(chr(9484) + chr(9472) * 12 + chr(9516) + chr(9472) * 12
                  + chr(9488))
            print(chr(9474) + "{:^12}".format("v") + chr(9474) +
                  "{:^12}".format("M") + chr(9474))
            print(chr(9500) + chr(9472) * 12 + chr(9532) + chr(9472) * 12
                  + chr(9508))
            # Function 3
            v = start
            flag = 1
            for i in range(n):
                if i + 1 == n:
                    flag = 0
                m = v**2 -25
                if m < m_min:
                    m_min = m
                if m > m_max:
                    m_max = m
                print(chr(9474) + "{:<12.5}".format(v) + chr(9474) +
                        "{:<12.5}".format(m) + chr(9474))
                # Check for last iteration
                if flag:
                    print(chr(9500) + chr(9472) * 12 + chr(9532) + chr(9472) * 12
                            + chr(9508))
                else:
                    print(chr(9492) + chr(9472) * 12 + chr(9524) + chr(9472) * 12
                            + chr(9496))
                v += shag
        else:
            print("Data error, try again")
            print()
            flag = int(input("Re-enter '1', End input '0' "))
            print()
            continue
        print()
        flag = int(input("Re-enter '1', End input '0' "))
        print()
    else:
        print("Data error, try again")
        print()
        flag = int(input("Re-enter '1', End input '0' "))
        print()
        continue

flag = 1
# Check on one point
if n == 1:
    print("You need at least two points to plot the chart!")
    print()
    flag = 0
# Plotting if more than one point
if flag:
    print("Plotting the function M = x^2 - 25")
    print("Plotting the function Y = sin(x) * x")
    print()
    x = start
    v = start
    os_min = min(y_min, m_min)
    os_max = max(y_max, m_max)
    os_delen = (os_max - os_min) / 6
    for i in range(0,7,1):
        if shag > 0:
            print("{:<15.4}".format(os_min + i*os_delen), end="")
        else:
            print("{:<15.4}".format(os_min - i*os_delen), end="")
    print()
    print(chr(9500) + chr(9472) * 14 + chr(9532) + chr(9472) * 14 + chr(9532) +
          chr(9472) * 14 + chr(9532) + chr(9472) * 14 + chr(9532) + chr(9472) *
          14 + chr(9532) + chr(9472) * 14 + chr(9532) + chr(9472))
    for i in range(n):
        m = v**2 - 25
        y = sin(x) * x
        razmetka1 = round((m - os_min) / (os_max - os_min) * 90)
        razmetka2 = round((y - os_min) / (os_max - os_min) * 90)
        if (finish >= 0 and start <= 0) or (start >= 0 and finish <= 0):
            null = round((0 - os_min) / (os_max - os_min) * 90)
        else:
            null = -1
        for i in range(91):
            if i == razmetka1:
                print(chr(42), end="")
            elif i == razmetka2:
                print(chr(42), end="")
            elif i == null:
                print(chr(9474), end="")
            else:
                print(" ", end="")
        print(" {:<12.4}".format(x))
        v += shag
        x += shag
    print()
input("To close the program, press 'Enter'")
