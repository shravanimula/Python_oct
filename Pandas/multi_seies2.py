import pandas as pd
student_series=pd.Series(['aaaa','bbbb','cccc','dddd'])
marks_series=pd.Series([11,22,33,44])
list1={'student':student_series,
        'marks':marks_series}
result=pd.DataFrame(list1)
rollno=[1,2,3,4]
result['rollno']=pd.Series(rollno)
print(result)
