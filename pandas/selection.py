import pandas as pd
df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv")
#SELECT BY COLUMN
#print(df["title"].to_string())
#print(df["publisher"].to_string())
#print(df[["title","year","publisher"]].to_string())

#SELECT BY ROW
#print(df.loc[0])

# to access row by title by make it label

df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv",index_col="title")
#print(df.loc["Sonic Mania"])
#print(df.loc["Sonic Mania",["year","publisher","platform"]])
#print(df.loc["Sonic Mania":"Shadow of the Colossus",["year","publisher","platform"]])
#print(df.iloc[0:11])
#print(df.iloc[0:11:2])
print(df.iloc[0:11:2,0:3])
print('-------------------------------')

#df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv",index_col="publisher")
#print(df.loc["Capcom"])


game = input("Enter game title : ")
try:
    print(df.loc[game])
except KeyError:
    print("f{game} not found")