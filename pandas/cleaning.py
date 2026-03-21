import pandas as pd 

# Data Cleaning = the process of fixing/removing :
#                  incomplete, incorrect or irrelevant data.
#                  ~75% of work done with pandas is data cleaning 
df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv")

# 1. Drop irrelevant columns
#df = df.drop(columns=["developer","rank"])
#print(df)

# 2. handle missing data 
#df = df.dropna(subset=["playtime"])
#df = df.fillna({"playtime":"FUCK"})
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