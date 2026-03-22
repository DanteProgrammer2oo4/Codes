import matplotlib.pyplot as plt
import numpy as np
# Bar Chart = compare categories of data representing each category with a bar

categories = ["grains","fruits","vegtables","protein","dairy","sweets"]
values = np.array([4,3,1,5,3,1])

#plt.barh(categories,values) # horizantial bar chart
plt.bar(categories,values,color="skyblue")
plt.title("Daily Consumption",
          size=30,
          color="#004910",
          fontweight="bold")
plt.xlabel("Food",
           size=20,
           color="red")
plt.ylabel("Quantity",
           size=20,
           color="brown")
plt.show()