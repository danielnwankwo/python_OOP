# creating an animal class as a Parent/Super/Base

class animal:
# initialising the animal class
    def __init__(self):
        self.alive = True  # creating the attributes
        self.spine = True
        self.lungs = True
        self.eyes = True

# creating the behaviours as functions/methods
    def breathe(self):
        return "must breathe to stay alive"

    def move(self):
        return "left to right and up and down"

    def eat(self):
        return"Nom Nom Nom"

    def procreate(self):
        return"find partner"

# instantiate th class/create an object

# creating the object of our animal class

cat = animal()
# cat has now inherited all attributes and functions from the parent(animal) class
# we have Abstracted eat() method from our parent class
# print(cat.eat())

print(cat.alive)
