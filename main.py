import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arrc = arr.copy()
arrv = arr.view()
arr[0] = 11
arrc[1] = 22
arrv[2] = 33
print(arr)
print(arrc)
print(arrv)
print(arrc.base)
print(arrv.base)