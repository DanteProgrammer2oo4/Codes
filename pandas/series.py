import pandas as pd
# series = A pandas 1-Dimensional labeled array that can hold any data type
# think of it like a simple column in a spreadsheet (1-Dimensional)
data = [100,102,104]
series = pd.Series(data)
print(series)

print('--------------------')

series = pd.Series(data,index=['a','b','c'])
print(series)
print()
print(series.loc["a"])
print(series.iloc[0])
print('---change value of c ------')
series.loc['c'] = 200
print(series)       


print('----------------------')
data = [100,102,104,200,202]
series = pd.Series(data,index=['a','b','c','d','e'])
print(series[series >= 200])

print('--------------------------------')
calories = {"Day 1":1750,"Day 2":2100,"Day 3":1700}
series = pd.Series(calories)
print(series)
print()
print(series.loc["Day 1"])
print()
series.loc["Day 3"] += 500
print(series.loc["Day 3"])
print()
print(series[series >= 2000])
print("------------------------------------")
n = (1.5,2,3,4,5,6)
series = pd.Series(n)
print(series)


