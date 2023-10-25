#local variable and class level variable can have the same name
class Test:
    a=10
    def func(a):
        print("the method variable a is:",a)
        print("the class variable a is:",Test.a)
        Test.a=Test.a+a

Test.func(20)
print("after modification the class value is:",Test.a)
