import pandas as pd
df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv")

#print(df.head(10))
#print(df.head()) first 5 rows

#print(df.tail())  last 5 rows


#print(df.info()) # information about data
#df.dropna(inplace = True) # Remove all rows with NULL values

df['Date'] = pd.to_datetime(df['date'], format='mixed')
print(df.to_string())