def factorial(num):
    fact=1
    if(num==0 or num==1):
        return 1
    for i in range(2,num+1):
        fact*=i
    return fact
num=int(input("enter a number:"))

result=factorial(num)
print("The factorial of", num, "is", result)