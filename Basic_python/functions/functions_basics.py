#FUNCTIONS:-  functions are a block of code that is used to perfrom a specific task. a function is devided into two parts:
    # 1. function definition: it is the part where we define the function using the def keyword followed by the function name and parentheses.
    # 2. function call: it is the part where we call the function to execute the
# IN PYTHON WE DEFINE A FUNCTION USING THE DEF KEYWORD FOLLOWED BY THE FUNCTION NAME AND PARENTHESES. block of code inside the function.
# SYNTAX:
# def function_name(parameters):
#     # block of code
#     return value
# EXAMPLE:
def greet():
    print("Hello, welcome to Python functions!")
# ALSO A FUNCTION CAN TAKE INPUT PARAMETERS AND RETURN OUTPUT VALUES USING THE RETURN STATEMENT 
# EXAMPLE:
def add_numbers(a, b):
    sum = a + b
    return sum
# FUNCTION CALL:
greet()  # calling the greet function
result = add_numbers(5, 10)  # calling the add_numbers function with arguments 5 and 10
print("The sum is:", result)  # Output: The sum is: 15
# FUNCTION WITH DEFAULT PARAMETERS:
def greet_user(name="Guest"):
    print("Hello,", name)   
greet_user()  # Output: Hello, Guest
greet_user("Alice")  # Output: Hello, Alice
print(type(add_numbers("roshan","chandola")))
