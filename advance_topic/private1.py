#access class level variable from outside class then its give error
class One:
    __a=10

class Two:
    def func():
        print("access the class private value is:",One.__a)

#AttributeError: type object 'One' has no attribute '_Two__a

Two.func()
