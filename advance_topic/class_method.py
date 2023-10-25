#class name method can be accessed using class name
class A:
    a=10
    def function():
        print("class member accessed in method:",A.a)

A.function()
