# class is a blueprint for creating objects. A class defines the attributes of the object and the methods (functions) that operate on those attributes. object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.
class Student :
    # constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # method to display student details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
# creating objects of the Student class
#  object1 created for class and involking constructor 
student1 = Student("Alice", 20, "A")   

student2 = Student("Bob", 22, "B")
student3 = Student("Charlie", 19, "A+")
student1.display_info()
student2.display_info()    
student3.display_info() 
