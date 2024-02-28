# this is a program to generate pascals triangle
# date : 23/2/2024
# name : elsie wanjiku

# print pascals triangle in python
from math import factorial

# input n
n = 5
for i in range (n):
    for j in range (n-i+1):

        # for left spacing
        print(end=" ")
        for j in range(i + 1):

            # nCr = n!/((n-r)!*r)
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

        # for new line
        print()
