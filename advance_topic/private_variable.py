#accress object level private variable within the class
class Test:
    def __init__(self,a):
        self.__a=a
        
    def display(self):
        print("private variable of a is:",self.__a)


obj=Test(10)
obj.display()
