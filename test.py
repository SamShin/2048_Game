import numpy as np

a = np.zeros((3,3))
b = np.zeros((3,3))

b[2][2] = 3

a = b

if np.array_equal(a, b):
    print("yes")
else:
    print("no")