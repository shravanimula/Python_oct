#super function allows us to call a parent method from the child class
class Parent:
    def func1(self):
        print("this ia the parent function")

class Child(Parent):
    def func2(self):
        super().func1()
        print("this is child function")

obj=Child()
obj.func2()
