class Parent():
    def func1(self):
        print("iam in parent class")


class Child(Parent):
    def func2(self):
        print("iam in child class")


var=Child()
var.func1()
var.func2()
