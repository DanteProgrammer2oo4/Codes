import pandas as pd
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_csv(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path)  # Read csv into DataFrame
df = load_csv("data.csv")

#print(df.head(10))
#print(df.head()) first 5 rows

#print(df.tail())  last 5 rows


#print(df.info()) # information about data
#df.dropna(inplace = True) # Remove all rows with NULL values

df['Date'] = pd.to_datetime(df['date'], format='mixed')
print(df.to_string())
