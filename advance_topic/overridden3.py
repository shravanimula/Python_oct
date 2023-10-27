class Parent1:
    def fun(self):
        print("parent1 function")

class Parent2:
    def fun(self):
        print("parent2 function")

class Child(Parent1,Parent2):
    def fun(self):
        print("child function")

    def display(self):
        self.fun()
        Parent1.fun(self)
        Parent2.fun(self)

ob=Child()
ob.display()
