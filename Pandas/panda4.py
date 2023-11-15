#Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns

import pandas as pd
school={
        'name':['aa','bb','cc','dd'],
        'marks':[60,65,70,75]
        }
studentsmarks=pd.DataFrame(school)
print(studentsmarks)
