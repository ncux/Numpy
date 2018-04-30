"""
numpy.arange
This function returns an ndarray object containing evenly spaced values within a given range.
The format of the function is as follows:
numpy.arange(start, stop, step, dtype)
The constructor takes the following parameters.
start The start of an interval. If omitted, defaults to 0
stop The end of an interval (not including this number)
step Spacing between values, default is 1
dtype
Data type of resulting ndarray. If not given, data type of input is used
"""

import numpy as np
x = np.arange(5)
print(x)

# dtype set
x = np.arange(5, dtype=float)
print(x)

# start and stop parameters set
x = np.arange(10,20,2)
print(x)
