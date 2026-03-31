import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_csv(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path)  # Read csv into DataFrame
df = load_csv("data.csv")
#SELECT BY COLUMN
#print(df["title"].to_string())
#print(df["publisher"].to_string())
#print(df[["title","year","publisher"]].to_string())

#SELECT BY ROW
#print(df.loc[0])

# to access row by title by make it label

#df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv",index_col="title")
def load_csvT(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path,index_col='title')  # Read csv into DataFrame

df = load_csvT("data.csv")
#print(df.loc["Sonic Mania"])
#print(df.loc["Sonic Mania",["year","publisher","platform"]])
#print(df.loc["Sonic Mania":"Shadow of the Colossus",["year","publisher","platform"]])
#print(df.iloc[0:11])
#print(df.iloc[0:11:2])
print(df.iloc[0:11:2,0:3])
print('-------------------------------')

#df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv",index_col="publisher")
def load_csvP(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path,index_col='publisher')  # Read csv into DataFrame

df = load_csvP("data.csv")

print(df.loc["Capcom"])

print('-------------------------------')


game = input("Enter game title : ")
try:
    print(df.loc[game])
except KeyError:
    print("f{game} not found")
