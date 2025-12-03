# tuples are same as list but they are immutable in nature and ordered. they also allow duplicate elements. it is data structure that can store a collection of items. to declare a tuple we use parentheses ().
# example of tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
# tuples are basically used to store multiple items in a single variable.
# accessing elements of tuple by using their index, indexing starts from 0.
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
# tuples are immutable, so we cannot modify elements of tuple
# adding elements to tuple is not possible as they are immutable
# removing elements from tuple is not possible as they are immutable
# slicing of tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)
# iterating through a tuple using for loop
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)
# finding length of tuple using len() function
print("Length of the tuple:", len(my_tuple))
# checking membership using 'in' keyword
print("Is 3 in the tuple?", 3 in my_tuple)
# print the index of an element using index() method
index_of_4 = my_tuple.index(4)  
print("Index of element 4 in the tuple:", index_of_4)
# counting occurrences of an element using count() method
count_of_2 = my_tuple.count(2)
print("Count of element 2 in the tuple:", count_of_2)
# concatenating two tuples
another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple)
# tuples support unpacking
# unpacking is a way to assign values from a tuple to multiple variables in a single statement.whereas list unpacking is similar but can be used with lists as well.
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
