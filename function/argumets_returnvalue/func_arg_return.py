#function with arguments and with return type

def function(n):
    fact=1
    while(n > 0):
        fact=fact*n
        n=n-1
    return fact


number=int(input("enter a number:"))
result=function(number)
print("factorial of{} is : {}".format(number,result))
