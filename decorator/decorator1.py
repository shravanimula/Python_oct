def addition(n1):
    def inner_addition(n2):
        return n1+n2
    return inner_addition

add=addition(2)
print(add(4))

add1=addition(4)
print(add1(4))
