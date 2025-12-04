''' In object oriented python programming, attributes are variables that belong to a class or an instance of a class. They are used to store data related to the object and can be accessed and modified using methods defined within the class. Attributes can be of various types, including instance attributes (specific to an instance), class attributes (shared across all instances), and static attributes (not tied to any instance).

They are basically of two types:
1. Instance Attributes: These attributes are specific to each instance of a class. They are defined within the constructor method (usually `__init__`) and are accessed using the `self` keyword.
2. Class Attributes: These attributes are shared across all instances of a class. They are defined directly within the class body and are accessed using the class name or through an instance.'''
class Student:
    # Class attributes
    school_name = "ABC High School" '''common attributs for all students'''
    school_address = "123 Main St"

    def __init__(self, name, age, cgpa):
        # Instance attributes
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, CGPA: {self.cgpa}")
        print(f"School: {Student.school_name}, Address: {Student.school_address}")
# Creating instances of the Student class
student1 = Student("Roshan", 19, 9.53)
student2 = Student("Anita", 19, 8.75)
# Displaying information for each student
student1.display_info() 
student2.display_info()
