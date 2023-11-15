#locate Row
#Pandas use the loc attribute to return one or more specified row(s)

import pandas as pd
school={
        'name':['aa','bb','cc','dd'],
        'marks':[60,65,70,75]
        }
studentsmarks=pd.DataFrame(school)
print(studentsmarks.loc[1])
