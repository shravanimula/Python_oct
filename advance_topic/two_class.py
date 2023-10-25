#we can define more than one class in the same file
class One:
    var=10
  
class Two:
    def fun():
        print("the value of  var is :",One.var)

Two.fun()
