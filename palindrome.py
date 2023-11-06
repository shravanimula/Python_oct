st1=input("enter a string:")
flag=0
for i in range(0,int(len(st1)/2)):
    if (st1[i] != st1[len(st1)-i-1]):
        flag=1

if(flag==1):
    print("string is not a palindrome:",st1)
else:
    print("string is palindome:",st1)


