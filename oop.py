#!/usr/bin/python3
"""
## OOP
Class
"""
class CreditCard:
    """A cusumer credit card

    The initial balance is zero

    customer name of the customer
    bank     name of the bank
    acnt     the account identifier
    limit    credit limit
    """

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit car instance"""
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """Return the name of the customer"""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name"""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number"""
        return self._acnt
    
    def get_limit(self):
        """Return credit card limit"""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, given that there is sufficient balance
        
        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount
    