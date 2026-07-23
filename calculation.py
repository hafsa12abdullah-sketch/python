import numpy as np

arr = np.array([10,20,30,40,50])
print(arr)

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr)

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90,100])
print (arr.sum())
print (arr.max())
print (arr.mean())
print (arr.min())

import numpy as np

a = np.array([20,50,90,33,77,94,223,12,50])
b= np.array([30,22,15,60,73,69,110,200,82])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

import numpy as np

arr = np.array([10,20,30,40,50])
print(arr.mean())
print(arr.max())
print(arr.min())

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[3])
print(arr[-1])
print(arr[4])
print(arr[-2])
print(arr[4])
print(arr[-3])
print(arr[0])

import numpy as np

arr = np.array([1,2,3,4,5])
print(np.sum(arr))

import numpy as np

arr = np.array([2,6,7,10,3,22])
print(arr.sum())

import numpy as np

matrix = np.array([1,2,3,]),([4,5,6])
print(matrix)

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)

print(matrix[0])      # First row
print(matrix[:, 1])   # Second column
print(matrix[1, 2])   # Row 2, Column 3

import numpy as np

matrix = np.array([
    [10,20,30,40,50,60],
    [40,50,60,70,80,90],
    [70,80,90,10,40,30],
    [100,110,120,130,140,150],
    [30,55,25,85,95,35],
    [70,45,65,15,35,65]
])

print(matrix[1,2])
print(matrix[0,3])
print(matrix[2,-4])
print(matrix[0,3])
print(matrix[0,-3])
print(matrix[2,-2])
print(matrix[1,-4])
print(matrix[-1,-1])
print(matrix[-1, -1])  # 140
print(matrix[-1, -3])  # 120
print(matrix[-2, -4])  # 80
print(matrix[-4, -5])  # 10
