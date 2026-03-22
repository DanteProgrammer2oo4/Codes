import numpy as np
array = np.array('A')
print(array.ndim)
print("\n-------------------------\n")
array = np.array(['A','B','C'])
print(array.ndim)
print("\n-------------------------\n")
array = np.array([['A','B','C'],
                  ['D','E','F'],
                  ['G','H','I']])
print(array.ndim)
print("\n-------------------------\n")
array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z','_']]])  # must be 3 elements (consistent num of elements)
print(array.ndim)
print(array.shape)   # output : (3,3,3)  -> 3 layers 3 rows 3 cols
print("\n-------------------------\n")
print(array[0][0][0]) # Chain indexing
print()
print(array[0,0,0]) # Multidimensional indexing
                    # faster than chain indexing
print("\n-------------------------\n")
word = array[0,2,2]+array[2,2,2]+array[1,0,2]+array[1,1,2]+array[2,1,0]+array[0,1,1]+array[2,2,2]+array[2,2,0]+array[1,1,2]+array[2,0,2]+array[1,2,2]+array[2,2,2]+array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word)