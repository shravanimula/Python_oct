class Parent:
    def fun(self):
        print("parent function")

class Child(Parent):
    def fun(self):
        super().fun()
        print("child function")

    def display(self):
        self.fun()

obj=Child()
obj.display()
