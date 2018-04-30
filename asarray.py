"""
asarray
This function is similar to numpy.array except for the fact that it has fewer parameters. This
routine is useful for converting Python sequence into ndarray.
"""
import numpy as np

# convert list to ndarray
x = [1,2,3]
a = np.asarray(x)
print(a)

# dtype is set
a = np.asarray(x, dtype=float)
print(a)

# ndarray from list of tuples
x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)
