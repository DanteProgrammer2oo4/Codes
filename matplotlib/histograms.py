import matplotlib.pyplot as plt
import numpy as np
# Histogram = A visual representation of distribution of quantitative data .
#               they group values into bins (intervals)
#               and counts how many fall in each range

scores = np.random.normal(loc=80, scale=10, size=100)  # loc = median , scale = st.dev.
scores = np.clip(scores, 0, 100)  # Any value less than min_value becomes min_value                                    
                                  # Any value greater than max_value becomes max_value
                                  # Values inside the range stay the same
plt.hist(scores, bins=10,  # 10 intervals
         color="lightgreen",
         edgecolor="black")

plt.title("Exam Scores", weight="bold")
plt.xlabel("Scores", color="purple")
plt.ylabel("number of students", color="DarkBlue")
plt.show()
