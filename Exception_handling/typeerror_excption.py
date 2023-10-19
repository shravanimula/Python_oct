a=input("enter number:")
b=int(input("enter b number:"))
try:
    result=a+b
except TypeError:
    print("Error is:","cannot add int and string")
