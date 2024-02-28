friends = ["Juliet," "Ivy," "Ryan," "Anne," "Sam"]

for friend in friends:
    print(friend)


    enemies = friends[:]

    enemies = friends[:] # copy one list into another
    print(enemies)

    fruits = ["Guava", "Lemon", "Orange", "Pineaple", "Strawberry"]

    #slice the list to get part of the list

    print(fruits[0:3])
    del fruits[0]

print(fruits)     

squares = [] # initializes an empty list

for x in range(0,11):
    squares.append(x**2)

    print(squares)