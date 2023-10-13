def function(n):
    while n > 0:
        yield n
        n=n-1


for i in function(15):
    print(i)
