class Parent:
    def __init__(self):
        print("parent constructor")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("child constructor")

obj=Child()
