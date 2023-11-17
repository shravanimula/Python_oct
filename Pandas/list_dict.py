'''
from_records() function of DataFrame changes structured data or records into DataFrames. It converts a structured ndarray, tuple or dict sequence, or DataFrame into a DataFrame object
 '''

import pandas as pd
data=[{'aaaa':11,'bbbb':22,'cccc':33},
        {'aaaa':'a','bbbb':'b','cccc':'c'}]
result=pd.DataFrame.from_records(data,index=['1','2']) 
print(result)
