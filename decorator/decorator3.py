def outer_fun():
    print("iam in outer function")

    def inner_fun1():
        print("iam in inner function1")

    def inner_fun2():
        print("iam in inner function2")

    inner_fun1()
    inner_fun2()

outer_fun()
