import numpy as np

a = np.array([1, 2, 3])
print(a)

# more than one dimension
b = np.array([[1, 2], [3, 4]])
print(b)

# minimum dimensions
c = np.array([1, 2, 3, 4, 5], ndmin=2)
print(c)

