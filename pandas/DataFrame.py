import pandas as pd
# DataFrame = A tabular data structure with rows and columns.(2 Dimensional)
# similar to an Excel spreadsheet

data = {"Name":["spongebob","patrick","squidward"],
        "Age":[30,35,50]}
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data,index=["Employee 1","employee 2","Employee 3"])
print(df)
print("-------------------")
print(df.loc["Employee 1"]) 
#print(df.iloc[0])
print("---------add a new column----------")
df["Job"] = ["cook","N/A","cashier"]
print(df)
print("------add new row-----------")
#new_row = pd.DataFrame([{"Name":"sandy","Age":18,"Job":"Engineer"}])

#new_row = pd.DataFrame([{"Name":"sandy",
#                        "Age":18,
#                        "Job":"Engineer"}],index=["Employee 4"])
#df = pd.concat([df,new_row])
#print(df)

print("-------------add new rows ------------")
new_rows = pd.DataFrame([{"Name":"sandy",
                         "Age":18,
                         "Job":"Engineer"}
                         ,{"Name":"Eugene",
                           "Age":60,
                           "Job":"Manager"      
                         }],index=["Employee 4","Employee 5"])
df = pd.concat([df,new_rows])
print(df)