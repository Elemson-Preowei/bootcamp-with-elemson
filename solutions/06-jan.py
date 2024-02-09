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
        self.petals = 0.0
        self.price = 0 

    def get_name(self):
        return self.name
    
    def set_petals(self, num):
        return self.petals += num

    def get_petals(self):
        return self.petals
    
    def set_price(self, amt):
        return self.price += amt

    def get_price(self):
        return self.price
