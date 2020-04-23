# 2019
# SumNumbers
# Powered by LGleba
"""
Calculate the sum of a series with accuracy eps,
foresee the number of operations
display a table of values with a given print step.
Input data: argument value, eps,
Max. number of iterations, print step
"""
# Argument X
x = float(input("Enter the value of argument X in the range 0 < x <= 1: "))
if 0 < x <= 1:
    # Eps
    eps = float(input("Enter Eps: "))
    # Maximum number of iterations
    n_max = int(input("Enter the maximum number of iterations n_max: "))
    # Printing step
    shag = float(input("Enter the print step shag: "))
    # Pseudo table
    print(chr(9484) + chr(9472) * 12 + chr(9516) + chr(9472) * 12 + chr(9516) +
          chr(9472) * 12 + chr(9488))
    print(chr(9474) + "{:^12}".format("Number") + chr(9474) + "{:^12}".format("Element") +
          chr(9474) + "{:^12}".format("Sum") + chr(9474))
    print(chr(9500) + chr(9472) * 12 + chr(9532) + chr(9472) * 12 + chr(9532) +
          chr(9472) * 12 + chr(9508))
    summa = 1
    print(chr(9474) + "{:<12}".format(1) + chr(9474) + "{:<12}".format(1) +
          chr(9474) + "{:<12}".format(summa) + chr(9474))
    chis1 = 3
    chis2 = x
    a = -chis1 * chis2
    slog = 3
    znak = -1
    kol = 2
    flag = 0
    while abs(a) > eps and kol <= n_max:
            summa += a
            if kol % shag == 0:
                print(chr(9500) + chr(9472) * 12 + chr(9532) + chr(9472) * 12 +
                      chr(9532) + chr(9472) * 12 + chr(9508))
                print(chr(9474) + "{:<12}".format(kol) + chr(9474) +
                      "{:<12.4}".format(a) + chr(9474) +
                      "{:<12.4}".format(summa) + chr(9474))
                flag = 1
            znak = -znak
            chis1 += slog
            slog += 1
            chis2 *= x
            a = znak*chis1*chis2
            kol += 1
            flag = 0
    print(chr(9492) + chr(9472) * 12 + chr(9524) + chr(9472) * 12 +
          chr(9524) + chr(9472) * 12 + chr(9496))
    if abs(a) > eps:
        print("Amount did not match")
    else:
        print("Sum converged, " + "Summa = {:.4}".format(summa) + " for {} iterations".format(kol-1))
else:
    print("You entered an invalid X value!")
