def mydiv(divi):
    def inner_fun(x,y):
        if x < y:
            x,y=y,x
        return divi(x,y)
    return inner_fun

@mydiv
def divi(a,b):
    return (a/b)


print(divi(2,4))
print(divi(4,2))
