class Grandfather:
    def __init__(self,name):
        self.grandfather=name
        

class Father(Grandfather):
    def __init__(self,fathername,gfname):
        self.fname=fathername
        Grandfather.__init__(self,gfname)


class Son(Father):
    def __init__(self,sonname,fname,gfname):
        self.sname=sonname
        Father.__init__(self,fname,gfname)

    def display(self):
        print("Grandfather name is :", self.grandfather)  
        print("Father name is :", self.fname)  
        print("Son name is :", self.sname)


a=Son("SN","FN","GFN")
print (a.grandfather)  
a.display()  
