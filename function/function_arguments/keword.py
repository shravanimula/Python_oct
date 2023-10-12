def keywordarg(name,rollno,marks,grade):
    print("name={}  rollno={}  marks={}  grade={}".format(name,rollno,marks,grade))



keywordarg(name="aaa",rollno=1,marks=88,grade='a')
keywordarg(grade='b',name='bbb',marks=77,rollno=2)
keywordarg(marks=66,grade='b',rollno=3,name='ccc')
