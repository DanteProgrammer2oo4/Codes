import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_excel(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to excel file
    return pd.read_excel(path)  # Read excel into DataFrame
df = load_excel("Customer Call List.xlsx")

df = df.drop_duplicates()

df = df.drop(columns = "Not_Useful_Column")

#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123._/")


df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace('[^a-zA-Z0-9]', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',n=2, expand=True)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')



#df = df.replace('N/a','')
#df = df.replace('NaN','')

df = df.fillna('')

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)

#Another way to drop null values
#df = df.dropna(subset="Phone_Number"), inplace=True)

df = df.reset_index(drop=True)

print(df)
