# FUNCTION WITH VARIABLE NUMBER OF ARGUMENTS:
def multiply_numbers(*args):
    product = 1
    for num in args:
        product *= num
    return product
result = multiply_numbers(2, 3, 4)
print("The product is:", result)  # Output: The product is: 24
# FUNCTION WITH KEYWORD ARGUMENTS:
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice       
# age: 30
# city: New York
