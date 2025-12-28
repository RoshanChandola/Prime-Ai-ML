'''encapsulation is one of the most importent pillar of oops. the main goal of encapsulation is to protect the data from outside world and to achieve data hiding. it restricts direct access to some of the object's components and can prevent the accidental modification of data.'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # Public attribute
        self.__balance = balance  # Public attribute
    def get_balance(self): # getter method
        return self.__balance
    def set_balance(self, amount): # setter method
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")


acc1=BankAccount("Roshan Chandola", 100000000000)
print(acc1.name)  # Accessing public attribute
acc1.set_balance(30000000000)  # Using setter method to update balance
print(acc1._BankAccount__balance)  # Accessing public attribute