# creating the python class to inherit from the snake

from snake_class import snake

class python(snake):

# creating functions from our python class
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


    def digest_large_prey(self):
        return "YUM "

    def climb(self):
        return " up we goooo"

    def shed_skin(self):
        return "time to grow up fast"

# creating the instance of our python class

python_object = python()

print(python_object.breathe()) # function from our animal class
print(python_object.hunt()) # function from our reptile class
print(python_object.use_venom()) # function from snake class
print(python_object.shed_skin()) # function from python class