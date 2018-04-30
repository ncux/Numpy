import numpy as np

# using array-scalar type
dt = np.dtype(np.int32)
print(dt)

"""The following examples show the use of structured data type. Here, the field name and the
corresponding scalar data type is to be declared."""
dt = np.dtype([('age',np.int8)])
print(dt)
# now apply it to ndarray object:
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a)

# file name can be used to access content of age column
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype=dt)
print(a['age'])

