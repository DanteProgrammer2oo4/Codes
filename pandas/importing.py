import pandas as pd
df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv")
# or 
# df = pd.read_json("data.json")
#print(df)
print(df.to_string()) # to print all rows to large data