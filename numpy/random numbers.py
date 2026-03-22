import numpy as np
rng = np.random.default_rng()
#                          seed=1   to reproduce same results
#print(rng.integers(1,9))
#print(rng.integers(low=1,high=7)) # low, high not necessary just to make it readable
#print(rng.integers(low=1,high=101,size = 3)) # random 3 numbers

#print(rng.integers(low=1,high=101,size=(3, 2)))
#                                       r  c

#np.random.seed(seed=1)

print(np.random.uniform(low= -1,high=1,size=(3,2)))  # Uniform distribution



print("\n-------------------------------\n")

rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

print("\n-------------------------------\n")
rng = np.random.default_rng()
fruits = np.array(["🍎","🍊","🍌","🥥","🍍"])
#fruit = rng.choice(fruits)
#print(fruit)

fruits = rng.choice(fruits,size=(3,3))
print(fruits)