import pandas as pd 
import os
# aggregate functions = Reduces a set of values into a single summary value 
#                       Used to summarize and analyze data
#                       Often used with groupby() function 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def load_csv(filename):
    path = os.path.join(BASE_DIR, filename)  # Build path to csv file
    return pd.read_csv(path)  # Read csv into DataFrame
df = load_csv("data.csv")
# whole dataframe
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count(numeric_only=True))
#print(df.std(numeric_only=True)) ???????????


# single column

#print(df["year"].mean())
#print(df["year"].sum()
#print(df["year"].min()
#print(df["year"].max()
#print(df["year"].count())
#print(df["year"].std())

group = df.groupby("publisher")

print(group["year"].min().to_string())




#**وظائف التجميع** = تقوم بتقليل مجموعة من القيم إلى قيمة ملخصة واحدة  
#تُستخدم لتلخيص وتحليل البيانات  
#غالبًا ما تُستخدم مع دالة `groupby()`

#**تفصيل المصطلحات:**

#- **وظائف التجميع (Aggregate Functions):** دوال رياضية تطبق على مجموعة من البيانات
#- **تقليل (Reduces):** تحويل متعدد القيم إلى قيمة واحدة
#- **قيمة ملخصة (Summary Value):** مثل المتوسط، المجموع، العدد، إلخ
#- **تلخيص وتحليل البيانات (Summarize and Analyze Data):** استخراج معلومات مفيدة من كميات كبيرة من البيانات
#- **دالة groupby():** دالة تجميع البيانات حسب فئات معينة ثم تطبيق دوال التجميع عليها

#**أمثلة على وظائف التجميع الشائعة:**
#- `sum()`: مجموع القيم
#- `mean()`: متوسط القيم  
#- `count()`: عدد القيم
#- `min()`: أصغر قيمة
#- `max()`: أكبر قيمة
#- `std()`: الانحراف المعياري
