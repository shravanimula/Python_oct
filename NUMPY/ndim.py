#the numpy arrays provides the 'ndim' attribute that returns an integer that is tell us how many dimensions array have

import numpy as np
a=np.array(1)
b=np.array([1,2,3,4])
c=np.array([[1,2,3,4],[5,6,7,8]])
d=np.array([[[11,22],[33,44]],[[55,66],[77,88]]])
print("signle element:\n",a)
print("1d-array:\n",b)
print("2d-array:\n",c)
print("3d-array:\n",d)
