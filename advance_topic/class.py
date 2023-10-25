class Institute:
    def __init__(self,course):
        self.course=course

    def whichcourse(self):
        print(self.course,"class is going on")

    def reception():
        first=Institute("C")
        two=Institute("Data structure")
        three=Institute("Python")
        

        two.whichcourse()
        three.whichcourse()
        first.whichcourse()


Institute.reception()
