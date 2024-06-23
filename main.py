import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[0])
print(arr2[1,1])

arr3 = np.array([1, 2, 3], dtype='S')
print(arr3, arr3.dtype)
