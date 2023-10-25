a=10
class Test:
    a=20
    def func():
        print("the global value:",a)
        print("local value of a:",Test.a)

Test.func()

