import json
import pandas as pd

with open("data12.json","r") as data_file:
    data =json.load(data_file)
    print(data)
    json_string = json.dumps(data)
    print(json_string)




# Important "json_file1.json" is with single dictonarie i.e. single record 
with open ('json_file1.json','r') as f:
    jsondata = json.loads(f.read())

print("")
print("")
df1=pd.json_normalize(jsondata,["certifications"],["organization","website","formed","founder"])
print(df1.to_string())
df1.to_csv("json_file1.csv",index=False)  # no indexes in csv file like 0 ,1,2 as we see in output


# Important "json_file2.json" is with multiple dictonaries (i.e. multiple records), which are inclosed in LIST
with open ('json_file2.json','r') as f:
    jsondata2 = json.loads(f.read())

print("")
print("")
df2=pd.json_normalize(jsondata2,["certifications"],["organization","website","formed","founder"])
print(df2.to_string())
df2.to_csv("json_file2.csv",index=False)   # no indexes in csv file like 0 ,1,2 as we see in output


