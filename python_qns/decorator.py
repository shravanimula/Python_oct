'''
A Python Decorator is a mechanism to wrap a Python function and modify
its behavior by adding more functionality to it. We can use @ symbol to call
a Python Decorator function.
'''
def mydiv(div):
    def inner_fun(x,y):
        if x < y:
            x ,y=y,x
        return div(x,y)
    return inner_fun

@mydiv
def div(a,b):
    return (a/b)


print(div(2,4))
print(div(4,2))
