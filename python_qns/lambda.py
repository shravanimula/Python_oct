#A lambda function can take any number of arguments, but can only have one expression.

add=lambda x,y:x+y

a=int(input("enter a number:"))
b=int(input("enter b number:"))
print(add(a,b))


x=lambda a,b :a*b
print(x(5,6))

y=lambda a,b,c:a+b+c
print(y(2,4,6))
