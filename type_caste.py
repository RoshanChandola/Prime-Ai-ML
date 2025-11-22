a=5.7
b=int(a)
print(a)  # Output: 5.7
print(b)  # Output: 5
#type casting float to int 
r="2345"
s=int(r)
print(r)  # Output: "2345"
print(s)  # Output: 2345

#type casting string to int
# there are two types of type casting in python: implicit and explicit type casting.
        #implicit type casting: In implicit type casting, Python automatically converts one data type to another without any user intervention.
x=10    # integer  
y=3.5   # float
z=x+y   # implicit type casting from int to float
print(z)  # Output: 13.5
print(type(z))  # Output: <class 'float'>   
        #explicit type casting: In explicit type casting, the user manually converts one data type to another using built-in functions like int(), float(), str(), etc.
a=7.9
int(a)  # explicit type casting from float to int 
print(a)  # Output: 7