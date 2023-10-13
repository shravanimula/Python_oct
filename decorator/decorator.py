'''
Decorator Functions:
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

Decorators are usually called before the definition of a function you want to decorate.
'''
def adding_msg(msg):
    def inner_fun(name):
        if name=='bbbb':
            print(name,"good morning")
        else:
            msg(name)

    return inner_fun

@adding_msg
def msg(name):
    print("hello",name)

msg('aaaa')
msg('bbbb')
msg('ccc')
