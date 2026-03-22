import matplotlib.pyplot as plt
import numpy as np
x = np.array([2023,2024,2025,2026])
y1 = np.array([20,25,30,15])
y2 = np.array([14,18,37,25])
y3 = np.array([10,20,30,14])

plt.title("Class size",fontsize=25,
                       family="Arial",
                       fontweight="bold",
                       color="#7700ff")

plt.xlabel("Year",fontsize=20,
                       family="Arial",
                       fontweight="bold",
                       color="#00b7ff")

plt.ylabel("Students",fontsize=20,
                       family="Arial",
                       fontweight="bold",
                       color="#d60000")

plt.tick_params(axis="both",  # both,x,y
                colors = "#128ff6")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xticks(x) # force x text to be only given numbers 
plt.show()  