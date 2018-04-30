"""
numpy.frombuffer
This function interprets a buffer as one-dimensional array. Any object that exposes the buffer
interface is used as parameter to return an ndarray.
numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)
The constructor takes the following parameters.
buffer Any object that exposes buffer interface
dtype Data type of returned ndarray. Defaults to float
count The number of items to read, default -1 means all data
offset The starting position to read from. Default is 0
"""

import numpy as np

s = 'Hello World'
a = np.frombuffer(s, dtype='S1')
# print(a)


