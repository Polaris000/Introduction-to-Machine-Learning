import numpy as np


a = np.eye(3)
print(a)
# prints identity matrix of order 3

b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(b[:2, 1:3])
# prints 2 3
#        6 7



#integer indexing of arrays

c = np.array([[1, 2], [3, 4], [5, 6]])

print(c[[0, 1, 2], [0, 1, 0]])


