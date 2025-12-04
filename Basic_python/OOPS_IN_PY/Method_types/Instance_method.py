'''methods are basically a block of code to perform a specific task related to the object of the class. There are mainly three types of methods in python OOPS:

1. Instance Methods: These methods operate on instances of the class and can access and modify the object's attributes. They take `self` as the first parameter, which refers to the instance calling the method.

2. Class Methods: These methods operate on the class itself rather than on instances. They take `cls` as the first parameter, which refers to the class. Class methods are defined using the `@classmethod` decorator and can access class attributes and other class methods.

3. Static Methods: These methods do not operate on instances or the class itself. They do not take `self` or `cls` as the first parameter. Static methods are defined using the `@staticmethod` decorator and are used for utility functions that are related to the class but do not need access to instance or class data.'''  

# Example of Instance Method
class laptop:
    Storage_type = "SSD"
    brand = "Dell"
    model = "XPS 13"
    def __init__(self,RAM, Storage):  
        self.RAM = RAM
        self.Storage =Storage
    def display_specs(self):  # Instance method
        print(f"Brand: {self.brand}, Model: {self.model}, RAM: {self.RAM}, Storage: {self.Storage} ({self.Storage_type})")
obj1 = laptop("16GB", "512GB")
obj1.display_specs()  # Output: Brand: Dell, Model: XPS 13, RAM: 16GB, Storage: 512GB (SSD)

          