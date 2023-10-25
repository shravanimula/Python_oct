class Test:
    a=10

    def function():
        a=20
        print("local of a is:",a)
        print("class level a is:",Test.a)

Test.function()
