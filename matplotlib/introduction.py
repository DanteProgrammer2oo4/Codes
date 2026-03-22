#import matplotlib
#print(matplotlib.__version__)
import matplotlib.pyplot as plt  #pyplot provides a user-frienly interface for plotting
'''
x = [2023,2024,2025,2026]
y = [20,25,30,15]

#plt.plot(y) # points for y axis
plt.plot(x,y)
plt.show()
'''
import numpy as np # same but faster than normal list
x = np.array([2023,2024,2025,2026])
y = np.array([20,25,30,15])

plt.plot(x,y)
plt.show()