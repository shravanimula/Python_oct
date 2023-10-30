'''
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
'''
import numpy as np
a=np.array([1,2,3,4,5])
b=a.copy()
a[0]=11
print("original array:",a)
print("copy array:",b)


a1=np.array([11,22,33,44,55])
b1=a1.view()
a1[0]=10
print("original array:",a1)
print("view array:",b1)



