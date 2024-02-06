class CreditCard:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.bal = 0

    def get_name(self):
        return self.name     
    
    def set_bal(self):
        self.bal += 1000

    def get_bal(self):
        return self.bal    

c = CreditCard("Elemson", "Access")

print(c.get_name())

c.set_bal()

print(c.get_bal())


