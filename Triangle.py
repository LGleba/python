# 2019
# Triangle
# Powered by LGleba
"""
Determine the lengths of the sides of a triangle
by given integer coordinates of points.

Find also the median drawn from the smallest corner of the triangle,
then enter the coordinates of one point and determine whether
it is inside the triangle or not.
If located, then find the distance from the point to
the largest remote side or its continuation.

Check if the triangle is rectangular
"""
# Import root function from Math module
from math import sqrt

print(" _____________________________________________________")
print("|Determine the lengths of the sides of a triangle")
print("|by given integer coordinates of points.")
print("|")
print("|Find also the median drawn from the smallest corner of the triangle,")
print("|then enter the coordinates of one point and determine whether")
print("|it is inside the triangle or not.")
print("|If located, then find the distance from the point to")
print("|the largest remote side or its continuation.")
print("|")
print("|Check if the triangle is rectangular")
print("|_____________________________________________________")

# Entering Coordinates
x1, y1 = map(int,input("|Enter the coordinates of 1 vertex X and Y "
                       "comma separated: ").split())
x2, y2 = map(int,input("|Enter the coordinates of 2 vertex X and Y "
                       "comma separated: ").split())
x3, y3 = map(int,input("|Enter the coordinates of 3 vertex X and Y "
                       "comma separated: ").split())
x0, y0 = map(int,input("|Enter point coordinates X and Y comma "
                       "separated: ").split())

print("|_____________________________________________________")

# Triangle length calculations
dl1 = sqrt((x1-x2)**2 + (y1-y2)**2)
dl2 = sqrt((x2-x3)**2 + (y2-y3)**2)
dl3 = sqrt((x1-x3)**2 + (y1-y3)**2)

# Error
pog = 1e-7

# Create a flag
flag = 1

# Check for the existence of a triangle
if ((y1-y2)*x3 + (x2-x1)*y3 + (x1*y2-x2*y1)) == 0:
    print("|The triangle does not exist!")
    flag = 0
if flag:
    dl_min = min(dl1, dl2, dl3)

    # Check if a right triangle
    if (abs(dl1**2 - dl2**2 + dl3**2) <= pog) \
            or (abs(dl2**2 - dl3**2 + dl1**2) <= pog) \
            or (abs(dl3**2 - dl1**2 + dl2**2) <= pog):
        print("|The triangle is rectangular")
    else:
        print("|The triangle is not rectangular")

    # Finding the coordinate of the middle of the
    # smallest length and the median itself
    if dl1 == dl_min:
        x_mid = (x1+x2)/2
        y_mid = (y1+y2)/2
        dl_midiana = sqrt((x_mid-x3)**2 + (y_mid-y3)**2)
    elif dl2 == dl_min:
        x_mid = (x2+x3)/2
        y_mid = (y2+y3)/2
        dl_midiana = sqrt((x_mid - x1)**2 + (y_mid - y1)**2)
    else:
        x_mid = (x1+x3)/2
        y_mid = (x1+x3)/2
        dl_midiana = sqrt((x_mid - x2)**2 + (y_mid - y2)**2)
    print("|Median = {:.3}".format(dl_midiana))

    # Check the point in the triangle (x-xa)*(yb-ya) - (y-ya)*(xb-xa) = 0
    if (((x0-x1)*(y2-y1) - (y0-y1)*(x2-x1)) *
        ((x3-x1)*(y2-y1) - (y3-y1)*(x2-x1)) >= 0) \
        and (((x0-x2)*(y3-y2) - (y0-y2)*(x3-x2)) *
            ((x1-x2)*(y3-y2) - (y1-y2)*(x3-x2)) >= 0)\
        and (((x0-x3)*(y1-y3) - (y0-y3)*(x1-x3)) *
            ((x2-x3)*(y1-y3) - (y2-y3)*(x1-x3)) >= 0):
        flag = 1
        print ("|Yes, the point is in the triangle")
    else:
        flag = 0
        print("|No, the point is not in the triangle")

    # If the point is in a triangle, then look for the greatest distance to the side
    if flag:
        per1 = abs((y2 - y1)*x0 - (x2 - x1)*y0 + x2*y1 - y2*x1) / \
               sqrt((y2 - y1)**2 + (x2 - x1)**2)
        per2 = abs((y3 - y2)*x0 - (x3 - x2)*y0 + x3*y2 - y3*x2) / \
               sqrt((y3 - y2)**2 + (x3 - x2)**2)
        per3 = abs((y3 - y1)*x0 - (x3 - x1)*y0 + x3*y1 - y3*x1) / \
               sqrt((y3 - y1)**2 + (x3 - x1)**2)
        perpen = max(per1, per2, per3)
        print("|The greatest distance = {:.3}".format(perpen))

print("|_____________________________________________________")
input("\tTo close the program, press 'Enter'")
