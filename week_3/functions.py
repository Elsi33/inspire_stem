def print_name():
    print("My name is Elsie Wanjiku")


#calling the function
print_name()    

def print_details(name , age, id, gender):
    print("I am {0} , {1} years old . My Id no is{2} and gender is {3}",format(name, age, id, gender))
    print_details("Elsie Wanjiku","18", "1111111" "female")
    
def sum_nums(x,y):
        return x + y

     
z = sum_nums(10,20)
print(z)

def prod_nums(x,y):
        return x * y
y = prod_nums(5,6)
print(y)



def print_odds(first_no, last_number):
      for i in range(first_no, last_number):
            print(i % 2)
       
print_odds(0,15)


def print_square(first_no,last_no):
      for i in range(first_no,last_no+1):
            print(i**2)
print_square(0,10)
print("\t")     


s = float(input("Enter the side : "))
def s_a_cube(s,):
      return ((s**6))
def print_cube(first_no,last_no):
     for i in range(first_no,last_no+1):
        print(i**3)      
print_cube(0,10)


def is_prime(num):
    if num <=1:
        return False
       
s = float(input("Enter the side :" ))
def s_a_cube(s,):
    return ((s ** 6))
print(s_a_cube(s))

import math
pi = float(math.pi)

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
def s_a_cylinder(r,h):
    return 2 * pi * r**2 + pi* 2*r *h
print(s_a_cylinder(r,h))

r = float(input("Enter the radius : "))
l = float(input("Enter the length : "))
def s_a_cone(r,l):
    return pi *r *l
print(s_a_cone(r,l))

r = float(input("Enter the radius : "))
def s_a_sphere(r):
    return 2 * pi * r**2
print(s_a_sphere(r))

r = float(input("Enter the radius : "))
def volume_sphere(r):
    return 4/3 * pi * r**3
print(volume_sphere(r))

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
def volume_cone(r,h):
    return 1/3 * pi * r**2 *h
print(volume_cone(r,h))

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))
def volume_cylinder(r,h):
    return pi * r **2 * h
print(volume_cylinder(r,h))

s = float(input("Enter the side :" ))
def volume_cube(s):
    return s**3
print(volume_cube(s))
