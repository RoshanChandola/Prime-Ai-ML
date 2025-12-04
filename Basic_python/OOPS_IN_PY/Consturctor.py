# Constructor is a special method in Python classes that is automatically called when an object of the class is created. It is typically used to initialize the attributes of the object. In Python, the constructor method is defined using the `__init__` method.
class Student:
    name,age= "",0
    # Constructor method
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

    # Method to display student details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Creating an object of the Student class
student1 = Student("Roshan", 20) 
student1.display()  # Output: Name: Roshan, Age: 20
# self is a reference to the current instance of the class and is used to access variables that belong to the class.the main purpose of self is to differentiate between instance variables (attributes) and local variables within methods.