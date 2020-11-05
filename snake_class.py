# creating a snake class as the child class of reptile to inherit functionalities


from reptile_class import reptile

class snake(reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = True

# creating functions for the snake class
    def use_tongue_to_smell(self):
        return "I use tongue to smell"


# instantiate this class/create an object

snake_object = snake()

print(snake_object.limbs)
print(snake_object.breathe())
