# instance method are functions defined inside a class that operate on instances of the class. They can access and modify the object's attributes and are called on an instance of the class. The first parameter of an instance method is always `self`, which refers to the instance calling the method.
class Student:
    name ="roshan"
    age="20"
    cgpa="9.53"
    def display(self):  # Instance method
        print(f"Name: {self.name}, Age: {self.age}")
Student1=Student()
Student1.display()  # Creating an instance and calling the method