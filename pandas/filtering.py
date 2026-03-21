import pandas as pd
# Filtering = Keeping the rows that match a condition 
df = pd.read_csv(r"C:\Users\eg\Downloads\vs code programs\pandas\data.csv")
#year = df[df["year"]>=2015]
#print(year.to_string())
genre = df[(df["genre"]=="Fighting") |   #or
           (df["genre"]=="Adventure")]

game = df[(df["platform"]=="PS3") &   #and
           (df["genre"]=="Adventure")]
print(game)