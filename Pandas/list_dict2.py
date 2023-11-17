'''
If there are no matching values and columns in the dictionary, then the NaN value will be inserted into the resulting Dataframe.
'''

import pandas as pd
data=[{'aaaa':11,'bbbb':22,'cccc':33,'dddd':44},
        {'aaaa':'a','bbbb':'b','cccc':'c'}]
result=pd.DataFrame(data) 
print(result)
