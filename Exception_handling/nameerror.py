def fun(x,y):
    temp=x
    x=y
    y=temp
    print("x=",x,"y=:",y)


a=int(input("enter a number:"))
b=int(input("enter b number:"))
func(a,b)
