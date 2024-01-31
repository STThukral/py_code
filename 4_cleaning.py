import pandas as pd
df = pd.read_csv('data_file1.csv')
print(df.to_string())

print(" Remove rows with null values")
new_df = df.dropna()

print(new_df.to_string())

print("inplace = True how to use to remove null value rows from same dataframe")
print("to remove null data from original data frame use inplace = True")
df=pd.read_csv('data_file1.csv')
print("Didn't used new_df i.e new data frame, used 'inplace' to remove it")
print(" in same 'df' dataframe")
df.dropna(inplace = True)  
print(df.to_string())



print("Replace null values with 130  using fillna")
df=pd.read_csv('data_file1.csv')
df.fillna(130,inplace = True)
print("So you will see all 170 line but the nul values repalced with 130")
print(df.to_string())



print(" Repalce only specified columns")
df=pd.read_csv('data_file1.csv')
df["Calories"].fillna(800,inplace = True)
print(df.to_string())



print("repalce empty values with Mean,Median and Mode")
df=pd.read_csv('data_file1.csv')
x=df["Calories"].mean()
df["Calories"].fillna(x,inplace = True)
print(df.to_string())



print("Correct date format")
df=pd.read_csv("data_file_dt.csv")
print(df.to_string())

print("Correct date format using to_datetime method")
print("date 2020118 and 20201226line 23 and 27 resp, will changed into date format")
print("Also correct Duration line 7 its 450 make it 45")
df = pd.read_csv("data_file_dt.csv")
df['Date']=pd.to_datetime(df['Date'])
df.loc[7,'Duration']= 45  # make duration 45 where 450
print(df.to_string())

print("As line 7 has got duraiton 450 , this will change it to 120")
df=pd.read_csv("data_file_dt.csv")
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x,"Duration"] =120
print(df.to_string())


print("check if file has got duplicates using duplicated() function")
print(" 12th row will be false other true as duplicate row at 12")
print(df.duplicated())
print("12 row will be rmoved using below function so there will be 11 and 13 no 12th row")
df.drop_duplicates(inplace =True)
print(df.to_string)
