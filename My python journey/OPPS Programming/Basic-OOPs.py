#Try oops programming in python
#creating a class(design) to create objects
"""In order to make a car, first we have to draw a design on paper or computer right? 
Then we have to decide it's color, seats, engine, speed etc.. 
all these plans and designs are called class.After confirming the desing we start making real cars. these real cars are objects.
all the variables and functions created in the class block are called class..we use the class/design to make real cars """
class Cat:
    def __init__(self, color, breed, age, location): # color, breed, age, location these are class parameters. we have to assing them with new variables.
        self.color = color # we linked paramaters to object variables like self.name = name
        self.breed = breed
        self.age = age
        self.location = location

    def sound(self):
        print("meow\t" * 3)

cat1 = Cat("Green", "Hybrid", 3 , "Dhaka")
cat2 = Cat("Blue", "Indigenus", 2 , "Bogra")
print(cat1.color)
print(cat1.breed)
print(cat1.age)
print(cat1.location)
print(cat1.sound())

print(cat2.color)
print(cat2.breed)
print(cat2.age)
print(cat2.location)

