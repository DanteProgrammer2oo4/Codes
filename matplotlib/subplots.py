import matplotlib.pyplot as plt
import numpy as np
# Figure = The entire canvas 🖼
# Ax = A single plot (subplot) 📈

# print(plt.subplots(2,2)) # tuble rows,cols
x = np.array([1,2,3,4,5])

figure, axis = plt.subplots(2,2)
axis[0,0].plot(x,x*2, color="red")
axis[0,0].set_title("x*2")

axis[0,1].plot(x,x**2, color="blue")
axis[0,1].set_title("x**2") 

axis[1,0].plot(x,x**3, color="green")
axis[1,0].set_title("x**3") 

axis[1,1].plot(x,x**4, color="purple")
axis[1,1].set_title("x**4") 

#axis[1,1].pie(x,x**4 )  #  can also use pie , scatter , bar , hist & mix them
#axis[1,1].set_title("x**4") 

plt.tight_layout()  # distance between them for better layout
plt.show()
