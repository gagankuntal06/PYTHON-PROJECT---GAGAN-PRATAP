# Write a NumPy program to concatenate element-wise two arrays of string

import numpy as np
x1 = np.array(['Python', 'PHP'], dtype=np.str)
x2 = np.array([' Java', ' C++'], dtype=np.str)
print("Array1:")
print(x1)
print("Array2:")
print(x2)
new_array = np.char.add(x1, x2)
print("new array:")
print(new_array)