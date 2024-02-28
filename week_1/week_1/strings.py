# strings in python
# name : elsie wanjiku
# date : 22/2/2024

city = "nairobi"

print(city[0]) 
print(city[1]) 
print(city[2]) 
print(city[3]) 
print(city[4])
print(city[5])
print(city[6]) 


# conver to uppercase


print(city)
print("\n") # prints a new line
print(city.upper())
name = "ELSIE WANJIKU"
print(name)
print(name.lower()) # converts string to lower case

town = "      Naivasha      "

print(town)
print("\t") # new tab
print(town.strip())

# add two strings

f_name = "Elsie"
s_name = "Wanjiku"

full_name =  f_name + s_name

print(full_name)

# replacing a character

fruit = "OrangOOOOO"

print(fruit.replace("O" , "Y"))

subject = "Physical:Sciences"
print(subject.split(":"))

age =30
height = 1.6

print("I am {0} years old and {1} meters tall " .format(age,height))

activity = "dancing"
print("My hobby is %s" %(activity))
   

height = 1.2333355
print("My height is  %5.3f"%(height))

age = 32
print("My age is  %d"%(age))



name = "Elsie Wanjiku"
print(len(name))

print(f"My full name is {name}")


course = "Electrical"
school = "Engineering"

print("I am studying{course} in the school of{school}" ,format course = )
