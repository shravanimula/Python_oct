import pandas as pd
data=[[1,5,8],[2,6,9],[3,7,10]]
result=pd.DataFrame(data)
result.columns=['c1','c2','c3']
print(result)
print(result.transpose())

