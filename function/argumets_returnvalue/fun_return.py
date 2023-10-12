#function without arguments and with return type

def function():
    num=int(input("enter a number:"))
    flag=0
    for i in range(2,(num//2)+1):
        if num % i == 0:
            flag=1

    return flag

result=function()
if(result == 1):
    print("number is not a prime number")

else:
    print("number is prime number")
