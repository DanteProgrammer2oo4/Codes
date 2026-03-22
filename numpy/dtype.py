# dtype = keyword argument that tells NumPy what kind of values are stored in an array 
#         otherwise numpy guesses the best data type based on your data 
#         manually setting dtype improves performance 
#         & is more memmory efficient (especially when working with large data sets)

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string(str_, <U#)
# object (object_)

import numpy as np
array = np.array([1,2,3,4,5],dtype=np.int8)          # int8 maximum number 127
print(array)
print(array.dtype)              #int64: 8bits = 1bite       8bits * 5 elements = 40
print(f"{array.nbytes} bites")

print("\n-----------------------")
array = np.array([1,2,3,4,5],dtype=np.float16)         
print(array)
print(array.dtype)       
print(f"{array.nbytes} bites")
print("\n-----------------------")
array = np.array([1,2,3,4,5,0],dtype=np.bool_)   # _ bool = numpy boolean       
print(array)
print(array.dtype)       
print(f"{array.nbytes} bites")
print("\n-----------------------")
array = np.array(['szoboszlai','ekitike','wirtz'],dtype=np.str_)   # <U1  number of strings
print(array)                                     #dtype="<U4"  to limit charchters
print(array.dtype)                            
print(f"{array.nbytes} bites")
print("\n-----------------------")
array = np.array([1,True,3.14,4,'ekitike',0],dtype=np.object_)        
print(array)
print(array.dtype)       
print(f"{array.nbytes} bites")
print("\n-----------------------")
array = np.array([1.5,2.55,3.6,4.1,5.9],dtype=np.float16)   
array = array.astype(np.int16)        # convert dtype
print(array)
print(array.dtype)       
print(f"{array.nbytes} bites")