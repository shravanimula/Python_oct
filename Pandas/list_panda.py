#we will create a list of lists and then pass it to the Pandas DataFrame function. Also, we will add the parameter of columns which will contain the column names
import pandas as pd
data=[['aaa',11],['bbb',22],['ccc',33]]
result=pd.DataFrame(data,columns=['name','rollno'])
print(result)
