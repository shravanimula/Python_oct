class Parent:
    def __init__(self,a):
        self.a=a

class Child(Parent):
    def __init__(self,a,b):
        Parent.__init__(self,a)
        self.b=b

obj=Child(10,100)
print("parent a value :",obj.a)
print("child b value :",obj.b)
