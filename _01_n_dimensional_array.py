import numpy as np

# ndarray
# 1d -> vektor [1, 2, 3, 4, 5]
# 2d -> matriks [[1,2], [3,4]]
# 3d -> tensor 

array_1dimensi = np.array([1, 2, 3])
print("array 1 dimensi: ")
print(array_1dimensi)

array_2dimensi = np.array([[1,2], [3,4]])
print("array 2 dimensi: ")
print(array_2dimensi)

array_3dimensi = np.array([ [[[1,2], [3,4]]] , [[[5,6], [7,8]]] ])
print("array 3 dimensi: ")
print(array_3dimensi)

