import numpy as np 

m1 = [[1, 0, 2, -1],
      [3, 0, 0, 5],
      [2, 1, 4, -3],
      [1, 0, 5, 0]]

m2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 10, 9]]


a1 = np.array(m1)
det1 = np.linalg.det(a1)
print(a1)
print(det1)

a2 = np.array(m2)
det2 = np.linalg.det(a2)
print(a2)
print(det2)