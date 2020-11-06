# Python OOP example lesson 

# Step 1 
- creating an animal class as our parent


```class animal:
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
```










# Step 2 
- creating a reptile class as a child class
- why? so we can inherit from our parent class
- Abstract

# Step 3
- create the snake class as the child class of the reptile class

# Step 4
- create the python class


- ``` __name__ ```   and   ``__main__``  are used to check if the code is run from current file/directly from a different file/importing it

- we will create 2 files and use   ``` __name__ ```   and  ``` __main__  ``  in both files and outcome with show the difference