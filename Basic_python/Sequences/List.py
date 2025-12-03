# list is sequence type that is mutable and ordered. It allows duplicate elements.it is data structure that can store a collection of items.to declare a list we use square brackets [].
# example of list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)  
# list are basically used to store multiple items in a single variable.
# accessing elements of list by using there index, indexing starts from 0.
print("First element:", my_list[0])
print("Last element:", my_list[-1])  
# modifying elements of list
my_list[2] = 10 
print("Modified list:", my_list)
# adding elements to list using append() method
my_list.append(6)
print("List after appending 6:", my_list)
# removing elements from list using remove() method
my_list.remove(4)
print("List after removing 4:", my_list)
# slicing of list
sliced_list = my_list[1:4]  
print("Sliced list (index 1 to 3):", sliced_list)
# iterating through a list using for loop
print("Iterating through the list:")
for item in my_list:
    print(item) 
# finding length of list using len() function
print("Length of the list:", len(my_list))  
# checking membership using 'in' keyword
print("Is 10 in the list?", 10 in my_list)  
# concatenating two lists
another_list = [7, 8, 9]
combined_list = my_list + another_list
print("Combined list:", combined_list)  
# adding a nwew element at specific index using insert() method
my_list.insert(2, 15)   
print("List after inserting 15 at index 2:", my_list)
# removing last element using pop() method      
popped_element = my_list.pop()
print("Popped element:", popped_element)