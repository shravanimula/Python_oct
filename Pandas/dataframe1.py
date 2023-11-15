import pandas as pd
school=[['a',1,66],['b',2,77],['c',3,88],['d',4,56]]
st_details=pd.DataFrame(school,columns=['name','rollno','marks'])
print(st_details)
