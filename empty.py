"""numpy.empty
It creates an uninitialized array of specified shape and dtype. It uses the following constructor:
numpy.empty(shape, dtype=float, order='C')
The constructor takes the following parameters.
Shape Shape of an empty array in int or tuple of int
Dtype Desired output data type. Optional
Order 'C' for C-style row-major array, 'F' for FORTRAN style column-major array
"""
import numpy as np

x = np.empty([3,2], dtype=int)
print(x)