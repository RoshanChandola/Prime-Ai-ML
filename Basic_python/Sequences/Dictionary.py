# Dictionary is a data structure that stores key-value pairs, allowing for efficient retrieval, insertion, and deletion of values based on their associated keys. In Python, dictionaries are implemented as hash tables, which provide average-case constant time complexity for these operations.
# example of dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Original dictionary:", my_dict)      
# accessing values in dictionary using keys
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))
# modifying values in dictionary
my_dict['age'] = 26
print("Modified dictionary:", my_dict)
# Dictionary are mutable, so we can add new key-value pairs and dictionary are unordered.
# Accessing the keys of the dictionary
info = {'name': 'Bob', 'age': 30, 'city': 'dehli'}
print(info.keys)
# values of dictionary
print(info.values)
# get method of dictionary
print(info.get('name')) 
# some more methods of dictionary
# adding new key value pair
info['profession'] = 'Engineer'
print("After adding new key-value pair:", info) 
# removing a key-value pair
del info['city']
print("After deleting key 'city':", info)   
# checking if a key exists
print("Is 'age' in dictionary?", 'age' in info)     
# iterating through dictionary
for key, value in info.items():
    print(f"{key}: {value}")    
# Output:
# Original dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Name: Alice   
# Age: 25
# Modified dictionary: {'name': 'Alice', 'age': 26, 'city': 'New York'}
# dict_keys(['name', 'age', 'city'])
# dict_values(['Bob', 30, 'dehli'])
# Bob
