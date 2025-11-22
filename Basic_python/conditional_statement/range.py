# # range function is a user defined function that is used to generate a sequence of numbers within a specified range. It is commonly used in loops to iterate over a set of values.
# # syntax: range(start, stop, step)
# # start: The starting value of the sequence (inclusive). Default is 0.
# for i in range(1, 11):  # generates numbers from 1 to 10
#     print(i)
# # stop: The ending value of the sequence (exclusive).
# for i in range(5):  # generates numbers from 0 to 4
#     print(i)
# # step: The difference between each number in the sequence. Default is 1.
# for i in range(0, 20, 5):  # generates numbers from 0 to 19 with a step of 5
#     print(i)    
# # Example: Using range in a for loop to print even numbers between 0 and 20
# for i in range(0, 21, 2):
#     print(i)
# # Example: Using range in a for loop to print numbers in reverse order from 10 to 1
# for i in range(10, 0, -1):
#     print(i)    
for ch in range(97,124):
    print(chr(ch))