class Grandfather:
    def fun(self):
        print("grand father function")

class Parent(Grandfather):
    def fun(self):
        print("parent function")

class Child(Parent):
    def fun(self):
        print("child function")

    def display(self):
        self.fun()
        super(Child,self).fun()
        super(Parent,self).fun()

ob=Child()
ob.display()
