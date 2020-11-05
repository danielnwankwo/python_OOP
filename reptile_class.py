# create a reptile class as a child class of animal class

# syntax to import the files and classes - from file_name import class_name
# from file_name import * - will import all files
from animal import animal

class reptile(animal):
    def __init__(self):

        super().__init__()  # super().__init__() syntax for super class, used to inherit everything from a parent class
        self.cold_blooded = True
        self.tretapod = True
        self.heart_chamber = [3, 4]
        

# creating functions for our reptile class
    def seek_heat(self):
        return "it is very cold"

    def hunt(self):
        return "i must have find food"

    def use_venom(self):
        return "if i got it im using it"


# time to create an object of our reptile class to utilise our functionalities of OOP

reptile_object = reptile()

# all functionalities inherited from animal class
print(reptile_object.eat)
print(reptile_object.breathe())
print(reptile_object.procreate())

# functionalities from current class
print(reptile_object.hunt())
print(reptile_object.use_venom())