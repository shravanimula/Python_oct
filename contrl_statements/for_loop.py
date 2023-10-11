num=int(input("enter number:"))
flag=0
for i in range(2,(num//2)+1):
    if num % i == 0:
        flag=1
if(flag==1):
    print("given number is not prime:",num)
else:
    print("given number is prime:",num)
