class Parent1:
    def __init__(self,a):
        self.a=a

class Parent2:
    def __init__(self,b):
        self.b=b

class Child(Parent1,Parent2):
    def __init__(self,a,b,c):
        Parent1.__init__(self,a)
        Parent2.__init__(self,b)
        self.c=c

    def display(self):
        print("a value:",self.a)
        print("b value:",self.b)
        print("c value:",self.c)

obj=Child(10,20,30)
obj.display() 
