import pandas as pd 
import os
# Data Cleaning = the process of fixing/removing :
#                  incomplete, incorrect or irrelevant data.
#                  ~75% of work done with pandas is data cleaning 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_csv(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path)  # Read csv into DataFrame
df = load_csv("data.csv")

# 1. Drop irrelevant columns
#df = df.drop(columns=["developer","rank"])
#print(df)

# 2. handle missing data 
#df = df.dropna(subset=["playtime"])
#df = df.fillna({"playtime":"0"})
#print(df.to_string())

# 3. Fix inconsistent values

#df["publisher"] = df["publisher"].replace({"Sony":"SONY",
#                                           "Sega":"SEGA"})


# 4. Standarize text
#df["title"] = df["title"].str.lower()


# 5. Fix data types   # used to change data from 1 , 0 to bool for example
#df["rank"] = df["rank"].astype(float)


# 6. Remove duplicates values

df = df.drop_duplicates()
print(df.to_string())
