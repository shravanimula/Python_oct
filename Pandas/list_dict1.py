'''
convert a list of dictionaries to a pandas DataFrame using pd.DataFrame.from_dict()
builds DataFrame from a dictionary of the dict or array type. By using the dictionary’s columns or indexes and allowing for Dtype declaration, it builds a DataFrame object.
 '''

import pandas as pd
data=[{'aaaa':11,'bbbb':22,'cccc':33},
        {'aaaa':'a','bbbb':'b','cccc':'c'}]
result=pd.DataFrame.from_dict(data) 
print(result)
