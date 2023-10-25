class One:
    a=10
    def __init__(self,a):
        self.a=a

    def display(self):
        a=20
        print("in method function:",a)
        print("in object the value of a is :", self.a)
        print("class value of a is:",One.a)

obj=One(30)
obj.display()
