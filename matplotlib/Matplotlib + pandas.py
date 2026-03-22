import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("matplotlib/data.csv")
type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index , type_count ,
         color="#11ffff",
         edgecolor="black")
plt.title("Number of pokemon by primary type")
plt.xlabel("count")
plt.ylabel("type")
plt.tight_layout()
plt.show()