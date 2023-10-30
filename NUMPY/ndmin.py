#ndmin:when array is created,you can define the number of dimensions
import numpy as np
a=np.array([1,2,3,4,5],ndmin=2)
print(a)
print('number of dimensions:',a.ndim)

b=np.array([11,22,33,44,55,66],ndmin=3)
print(b)
print('number of dimensions:',b.ndim)
