def fun():
    yield 11.1
    yield 10
    yield "aaa"

for i in fun():
    print(i)
