# a program that gets the sum of the first 20 numbers
sum_nums= 0
max_value = int(input("Enter the max value :"))

for x in range(0,max_value + 1):
    sum_nums = sum_nums + x
print(sum_nums)
