# 2019
# Cylinder
# Powered by LGleba
"""
Meaning:
	According to the given parameters, determine the volume,
	total and lateral surface area of the cylinder.
Condition:
	15) The cylinder has a section. Find the area of the full and lateral surface
        and volume from base to section. Given: R, H, l1, l2.
        Find: V, S full, S lateral.
"""
# Import the Math module
from math import pi

print(" ________________________________________________________________")
# Greeting
print("|\t\t\tThe solution of the problem")
# Task description
print("|\t\tAccording to the given parameters, determine the volume,") 
print("|\t\ttotal and lateral surface area of the cylinder.")
print("|________________________________________________________________")

# Flag for catching negative numbers
flag = 1

# Negative Number Cycle
while flag:
	# Radius input
	R = float(input("|Enter the radius of the cylinder: R = "))
	
	# Height input
	H = float(input("|Enter cylinder height: H = "))
	
	# Enter distance 1
	l1 = float(input("|Enter distance 1 from " +\
				"base to the cylinder section: l1 = "))
	# Enter distance 1 2
	l2 = float(input("|Enter distance 2 from " +\
				"base to the cylinder section: l2 = "))
	
	# Check for negative numbers
	if ((R < 0) or (H < 0) or (l1 < 0) or (l2 < 0)):
		print("|________________________________________" +\
			"________________________")
		print("|\t\t\tThe data is incorrect!")
		print("|\t\t\tTry again")
		print("|________________________________________" +\
			"________________________")
		flag = 1
	else: 
		flag = 0
	
print("|________________________________________________________________")
print("|\t\t\tGreat, the data is recorded!")
print("|________________________________________________________________")

# Calculations

# We consider the base area of the cylinder
Sos = pi*R*R
# We consider the area of the lateral surface of the cylinder
Sb = 2*pi*R*H
# We consider the total surface area of the cylinder
Sp = 2*Sos + Sb
# We consider the volume of the cylinder from the base to the section
V = Sos * (l1+l2)/2 

# Output the results
print("|The total surface area of the cylinder: Sp = {0:.4}".format(Sp))
print("|The area of the lateral surface of the cylinder: Sb = {0:.4}".format(Sb))
print("|Cylinder volume from base to section: V = {0:.4}".format(V))
print("|________________________________________________________________")
input("\t\tTo close the program, press 'Enter'")
