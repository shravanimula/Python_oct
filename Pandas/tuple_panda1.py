#we will use the df.from_records() to create the dataframe from the list of tuples.

import pandas as pd
record=[('aa',1,11),
        ('bb',2,22),
        ('cc',3,33),
        ('dd',4,44),
        ('ee',5,55)]
result=pd.DataFrame.from_records(record,columns=['name','rollno','marks'])
print(result)
