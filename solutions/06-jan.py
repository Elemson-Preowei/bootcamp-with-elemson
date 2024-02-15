"""
# Assignment 1
----------------------------------------------------------------------------
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number 
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""

class Flower:
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = 0
        self.price = 0.0 

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_petals(self, num):
        self.petals = num

    def get_petals(self):
        return self.petals
    
    def set_price(self, amt):
        self.price = amt

    def get_price(self):
        return self.price

habiscus = Flower("habiscus", 5, 1000.00)
habiscus.set_name("rose")
print(f"The flower on sale is {habiscus.get_name()}")