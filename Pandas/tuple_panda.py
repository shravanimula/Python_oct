import pandas as pd
record=[('aa',1,11),
        ('bb',2,22),
        ('cc',3,33),
        ('dd',4,44),
        ('ee',5,55)]
result=pd.DataFrame(record,columns=['name','rollno','marks'])
print(result)
