import pandas as pd
import os
# Filtering = Keeping the rows that match a condition 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_csv(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path)  # Read csv into DataFrame
df = load_csv("data.csv")

#year = df[df["year"]>=2015]
#print(year.to_string())
genre = df[(df["genre"]=="Fighting") |   #or
           (df["genre"]=="Adventure")]

game = df[(df["platform"]=="PS3") &   #and
           (df["genre"]=="Adventure")]
print(game)
