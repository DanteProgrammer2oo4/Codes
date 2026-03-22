import numpy as np
# Broadcasting allows NumPy to perform operations on arrays 
# with different shapes by virtually expanding dimensions 
# so they match the larger array's shape 

# the have the same size 
# or
# one of dimenstions have a size of 1

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

print("\n-----------------------\n")
array1 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)
print("\n-----------------------\n")
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1 * array2)