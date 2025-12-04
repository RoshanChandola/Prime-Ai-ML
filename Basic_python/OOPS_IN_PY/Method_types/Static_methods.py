'''static methods are functions defined inside a class that do not operate on instances of the class. They do not have access to the instance (`self`) or class (`cls`) variables. Static methods are defined using the `@staticmethod` decorator and can be called on the class itself without creating an instance.
defined using the @staticmethod decorator.
we use static methods when we need a utility function that is related to the class but does not require access to instance or class data.'''
class MathOperations:
    roshan="roshan"
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        print(f"The value of roshan is {MathOperations.roshan}")
        return a * b
# Calling static methods without creating an instance
sum_result = MathOperations.add(5, 3)
product_result = MathOperations.multiply(4, 2)
print(f"Sum: {sum_result}")          # Output: Sum: 8
print(f"Product: {product_result}")  # Output: Product: 8   
