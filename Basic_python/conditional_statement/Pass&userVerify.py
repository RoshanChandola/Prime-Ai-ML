username=input("Enter username: ")
password=input("Enter password: ")  
if username=="admin" and password=="pass123":
    print("Access granted")
elif username!="admin":
    print("invalid username")
else:
    print("invalid password")