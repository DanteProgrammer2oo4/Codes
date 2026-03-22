import numpy as np

# Scalar arthemetic    Scalar linear algebra term means single value

array = np.array([1,2,3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

print("\n-------------------------\n")

# Vectorized math funcs
array = np.array([1.01,2.5,3.99])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.pi)

print("\n-------------------------\n")
#Exercise

radi = np.array([1,2,3])
print(np.pi * radi ** 2)

print("\n-------------------------\n")

# Element-wise arthmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)


print("\n-------------------------\n")
# comparison operators
scores = np.array([91,55,100,75,82,64])

print(scores == 100)
print(scores > 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)