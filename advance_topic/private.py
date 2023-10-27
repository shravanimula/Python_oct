#we can access private variable only with in the class
class Test:
    __a=10
    def fun():
        print("the private variable is :",Test.__a)


Test.fun()
