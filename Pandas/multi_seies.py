import pandas as pd
data1=['aaaa','bbbbb','cccc','dddd']
data2=[11,22,33,44]
result1=pd.Series(data1)
result2=pd.Series(data2)
final={'data1':result1,
        'data2':result2}
output=pd.DataFrame(final)
print(output)
