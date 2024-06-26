import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
# x = [True, True, False, True, False, True]
# print(arr[x])

ll = []
for i in arr: ll.append(True) if i%2==0 else ll.append(False)

print(ll)
print(arr[ll])