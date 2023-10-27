#protected variable can be accessed only if parent-child relation is present
class Parent:
    def __init__(self,a,b):
        self.a=a
        self._b=b#protected variable

class Child(Parent):
    def display():
        obj=Parent(10,20)
        print("public variable of a is:",obj.a)
        print("protected variable of b is:",obj._b)

    
Child.display()
