'''a class method is defined with the @classmethod decorator and takes cls as the first parameter, which refers to the class itself. Class methods can access and modify class attributes and are often used for factory methods that create instances of the class using alternative constructors.
we use class methods when we need to work with class-level data or when we want to provide alternative ways to create instances of the class.
by using decorator @classmethod we can define a class method.
it can only access the class variables and other class methods inside the class.not the instance variables.
'''
class Circle:
    pi = 3.14159  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    @classmethod
    def  from_diameter(cls, diameter):
        print(f"the value of pi is {cls.pi}")
        radius = diameter / 2
        return cls(radius)  # Create an instance using the class
# Creating an instance using the class method
circle1 = Circle.from_diameter(10) 
print(f"Radius of circle1: {circle1.radius}")  # Output: Radius of circle1: 5.0
print(f"Value of pi: {Circle.pi}")  # Accessing class attribute
