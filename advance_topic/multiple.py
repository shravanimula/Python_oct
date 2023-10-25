class ClassA:
    def display(self):
        print('In Class A')
                    

class ClassB:
    def display(self):
        print('In Class B')

class ClassC(ClassA, ClassB):
    def display(self):
        ClassA.display(self)
        ClassB.display(self)
        print('In Class C')



a=ClassC()
a.display()
