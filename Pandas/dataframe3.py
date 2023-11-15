import pandas as pd
details={'name':['aa','bb','cc'],
        'maths':[55,66,77],
        'physics':[66,77,88] }
result=pd.DataFrame(details)
print(result)
print(result.transpose())
