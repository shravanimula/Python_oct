num=int(input("enter a number:"))
rev=0
temp=num
while(temp!=0):
    rev=rev*10+temp%10
    temp=temp//10

if(num==rev):
    print("given number is palindrome")

else:
    print("given number is not a palindrome")
