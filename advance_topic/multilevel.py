class Grandfather:
    def func1(self):
        print("this is grandfather function")

class Parent(Grandfather):
    def func2(self):
        print("this is parent function")

class Child(Parent):
    def func3(self):
        print("this is child function")


object=Child()
object.func1()
object.func2()
object.func3()
