# Lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. The syntax of a lambda function is as follows:
# SYNTAX:
# lambda arguments: expression      
# EXAMPLE:
# A lambda function that adds 10 to the input argument
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15
# A lambda function that multiplies two arguments
multiply=lambda a,b:a*b
print(multiply(2,3))  # Output: 6   
# A lambda function that returns the maximum of two arguments
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # Output: 20
# A lambda function that concatenates two strings       
concat = lambda str1, str2: str1 + " " + str2
print(concat("Hello", "World"))  # Output: Hello World
