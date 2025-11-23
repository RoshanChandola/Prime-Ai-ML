# strings are immutable, we can access each character using indexing.
# EXAMPLE:      
str=input("Enter a string: ")
length=len(str)
for i in range(length):
    print("Character at index",i,"is",str[i])
