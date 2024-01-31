import pandas as pd
df = pd.read_csv('data_file1.csv')
#print(df)
print(df.to_string())

d_string = "2023-09-17 14:30:00"
 
# Convert the string to datetime
dt_obj = pd.to_datetime(d_string)
 
print(dt_obj)

print("New lines can be created with backslash \n sharad")
