#to access global variable inside the function using global keyword
a=10
class Test:
    a=20
    def func():
        global a
        print("the global value:",a)
        a=a+30
        print("class variable of a:",Test.a)

Test.func()
print("after modification the global value:",a)
print("class value a:",Test.a)
