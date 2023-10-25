class Parent():  
    def fun1(self):  
        print ("parent class")  


class Child1(Parent):  
    def fun2(self):  
        print ("child1 class")  
        

class Child2(Parent):  
    def fun3(self):  
        print ("child2 class")  


var1 = Child1()  
var2 = Child2()  
var1.fun1()  
var1.fun2()  
var2.fun1()  
var2.fun3() 
