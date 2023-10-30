import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
print(a)
print(a[1:5])

print("printing the 4th element onwards:\n",a[4:])
print("starting elements :\n",a[:5])
print("print last elements using slicing:\n",a[-4:-1])
print("step:\n",a[1:6:2])
