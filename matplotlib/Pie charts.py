import matplotlib.pyplot as plt
import numpy as np

# Pie chart = circular chart divided into slices to show precentages of total.
#             Good for visualizing distribution among categories.

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300,250,275,225]) 
colors = ["red","yellow","blue","green"]
plt.pie(values, labels=categories,
                autopct="%1.1f %%", # double % to add %    -- .f without limit  -- n.f to limit numbers after (.)
                colors= colors,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=90 #rotate
                )

plt.title("IT dep.")
plt.show()