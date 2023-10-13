def function():
    yield "aaaa"
    yield 10
    yield 1.1

result=function()
print(next(result))
print(next(result))
print(next(result))
