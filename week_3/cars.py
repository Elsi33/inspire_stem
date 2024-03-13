cars = {"color":"black", "weight":"2175kg", "type":"mercedes benz", "speed":"316km/h"}
print(cars)

"""
for key.value in cars.items():
    print(key)
    print("\n")
    print(value)
"""


# this is  a class that describes cars

class car:
     def __innit__(self,model,make,year_of_production,fuel_capacity,color,horse_power):
          self.model = model
          self.make = make
          self.year_of_production = year_of_production
          self.fuel_capacity = fuel_capacity
          self.color = color
          self.horse_power = horse_power

     def print_make(self,make):
         print("The car is of {0} make".format(self,make))

    
     def self_make(self,make):
          self.make = make

     def get_make(self):
          return self.make     

my_car = car("Impala ","Chevrolet", "1969", "2500 cc",  )

friends_car = car("Note", "Nissan", "2014", "1400 cc", )   

my_car.print_make("Nissan")
         
my_car.set_make("Ford")
friends_car.set_make("Toyota")

print(my_car.get_make())
print(friends_car.get_make())
    