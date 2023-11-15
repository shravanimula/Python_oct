#index:the index argument, you can name your own indexes.
import pandas as pd
school={
        'class':[6,7,8,9],
        'members':[44,55,66,22]
        }
result=pd.DataFrame(school,index=['day1','day2','day3','day4'])
print(result)

