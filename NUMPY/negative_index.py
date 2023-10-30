#the negative indexing to access an array from the end
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("last element from 2nd dim:",arr[1,-1])
print("last element on 1st row:",arr[0,-1])
print("3rd element on 1st row:",arr[0,-2])
