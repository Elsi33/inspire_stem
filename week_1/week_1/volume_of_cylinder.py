# this is a program  to get the volume of a cylinder
# date : 22/2/2024
# name : elsie wanjiku

import math
r = float(input("enter the radius of the cylinder :"))
h = float(input("enter the height of the cylinder :"))

volume = ((2 * math.pi * (r**2)) + (math.pi * (2*r) * h))
print("the value of the volume is ",volume)