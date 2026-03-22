import numpy as np
array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
# array[start:end:step]
print(array[0:3])
print("\n-------------------------\n")
print(array[1:4])
print("\n-------------------------\n")
print(array[0:4:2])
print("\n-------------------------\n")
print(array[::2])
print("\n-------------------------\n")
print(array[2])
print("\n-------------------------\n")
print(array[::-1])
print("\n-------------------------\n")
print(array[::-2])
print("\n-------------------------\n")
print(array[:,0]) #print all rows in col 0
print("\n-------------------------\n")
print(array[:,0:3]) # first 3 cols
print("\n-------------------------\n")
print(array[:,1:4])
print("\n-------------------------\n")
print(array[:,1:])
print("\n-------------------------\n")
print(array[:,::2])
print("\n-------------------------\n")
print(array[:,1::2])
print("\n-------------------------\n")
print(array[:,::-1]) # reverse cols order
print("\n-------------------------\n")
print(array[0:2,0:2])
#           r    c
print("\n-------------------------\n")
print(array[0:2,2:])
print("\n-------------------------\n")
print(array[2:,0:2])