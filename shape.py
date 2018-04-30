"""ndarray.shape
This array attribute returns a tuple consisting of array dimensions. It can also be used to
resize the array."""

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)

# resize the ndarray
a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)
