# this is a program that shows how to get the hire purchase price
# date : 2/21/2024
# name : elsie wanjiku

d = float(input("enter the amount of the deposit"))
i = float(input("enter the amount paid in each installment"))
m = float(input("enter the installment period in months"))

price = d + (i * m)
print("total hire purchase price is ",price)
