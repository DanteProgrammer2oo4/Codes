import numpy as np
# Save a NumPy array
#array = np.array([[1,2,3],
#                 [4,5,6]])

#np.save('data',array)
#print(" NumPy array was saved !")


# Load a Numpy array
#array = np.load(r'C:\Users\eg\Downloads\vs code programs\numpy\data.npy')
#print(array)

# Save multiple NumPy array

#array1 = np.array([[1,2,3],
#                  [4,5,6]])
#array2 = np.array([1.1,1.2,1.3,1.4])
#array3 = np.array([2024,2025,2026,2027])
#np.savez(r'C:\Users\eg\Downloads\vs code programs\numpy\data.npz',array1,array2,array3)

#np.savez_compressed(r'C:\Users\eg\Downloads\vs code programs\numpy\data2.npz',array1,array2,array3) # use less memory
#print(" NumPy array was saved !")



# Load multiple NumPy array

arrays = np.load(r'C:\Users\eg\Downloads\vs code programs\numpy\data.npz')
array1 = arrays['arr_0']
array2 = arrays['arr_1']
array3 = arrays['arr_2']
print(array2)