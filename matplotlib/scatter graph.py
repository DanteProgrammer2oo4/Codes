import matplotlib.pyplot as plt
import numpy as np
# scatter graph = shows the relationship between two variables 
#                  helps to identify a correlation (+, -, None)
#                  example : Study hours vs. Test scores

x1 = np.array([0,1,1,2,3,4,5,6,7,7,8]) # Hours studied
y1 = np.array([55,60,65,62,68,70,75,78,82,85,88])  # Grades

x2 = np.array([0,1,2,2,3,4,5,6,7,8,8])
y2 = np.array([50,60,57,68,70,75,85,80,90,95,92])
plt.scatter(x1, y1, color="skyblue",
                  alpha=0.5, # transparency
                  s=100, # size 
                  label="class A"
                  )
plt.scatter(x2,y2, color="#eb5b67",
                  alpha=0.5,
                  s=100,
                  label="class B"
                  )
plt.title("Test Scores",
          size=30,
          color="#001986")
plt.xlabel("Hours studied",
           size=20,
           color="#6300C0")
plt.ylabel("Grades",
           size=20,
           color="#720000")
plt.legend()
plt.show()