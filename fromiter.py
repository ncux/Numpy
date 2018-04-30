"""
numpy.fromiter
This function builds an ndarray object from any iterable object. A new one-dimensional array
is returned by this function.
numpy.fromiter(iterable, dtype, count=-1)
Here, the constructor takes the following parameters.
iterable
dtype
Any iterable object
Data type of resultant array
28NumPy
The number of items to be read from iterator. Default is -1 which means all data
to be read
"""

import numpy as np

# create list object using range function
list = range(5)
print(list)

it = iter(list)

# use iterator to create ndarray
x = np.fromiter(it, dtype=float)
print(x)