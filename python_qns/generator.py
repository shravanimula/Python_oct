def func():
    a=10
    b=20
    yield a+b
    a=11
    b=22
    yield a+b

result=func()
print(next(result))
print(next(result))
