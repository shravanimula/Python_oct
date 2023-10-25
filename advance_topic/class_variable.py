class Test:
    a=10
    def function1():
        print("the value of a is:",Test.a)
        Test.a+=10
        Test.function2()

    def function2():
        print("the value a:",Test.a)

Test.function1()
