import json
import pandas as pd

with open("data12.json","r") as data_file:
    data =json.load(data_file)
    print(data)
    json_string = json.dumps(data)
    print(json_string)


fields   = data.keys()
values   = data.values()
bindvars = "'"+"','".join(values)+"'"
print(bindvars)


print(" getting simple dictonary to column_name and Values")
print("")
sqlstatement=''
TABLE_NAME='TAB1'
keylist = "("
valuelist = "("
firstPair = True
with open ('json_file1.json','r') as f:
    jsondata = json.loads(f.read())

#print(jsondata)
print(json.dumps(jsondata, indent=4))

for json_k,json_v in jsondata.items():
     if not firstPair:
            keylist += ", "
            valuelist += ", "
     firstPair = False
    #print(json_k)
    #print(json_v)
   
     keylist += json_k
     valuelist += "'" + str(json_v) + "'"
        
keylist += ")"
valuelist += ")"
    
print(f'column_names :{keylist}')
print(f'values : {valuelist}')
sqlstatement = "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist +" "
print("")
print(sqlstatement)






print(" getting simple dictonary to column_name and Values")
print("")
sqlstatement=''
TABLE_NAME='TAB1'
keylist = "("
valuelist = "("
firstPair = True
with open ('json_file1.json','r') as f:
    jsondata = json.loads(f.read())

#print(jsondata)
print(json.dumps(jsondata, indent=4))

for json_k,json_v in jsondata.items():
     if not firstPair:
            keylist += ", "
            valuelist += ", "
     firstPair = False
    #print(json_k)
    #print(json_v)
     if json_k == "certifications":
          print(f' json_v : {json_v}')
             # for cert_k,cert_v in json_k.items():
             #      print (f' cert_k : {cert_k}')
         
     keylist += json_k
     valuelist += "'" + str(json_v) + "'"
        
keylist += ")"
valuelist += ")"
    
print(f'column_names :{keylist}')
print(f'values : {valuelist}')
sqlstatement = "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist +" "
print("")
#print(sqlstatement)

#df=pd.json_normalize(jsondata)
#print(df.to_string())
#df.to_csv("json_file1.csv",index=False)

new_data = dict()
list2 = []
for json_k,json_v in jsondata.items():
     #print(isinstance(json_v,list))
     if not isinstance(json_v,list):
          new_data[json_k] = json_v
n=0
for json_k,json_v in jsondata.items():
     if isinstance(json_v,list):
          for i in json_v:
               #print(i)
               for k,v in i.items():
                    #print(isinstance(v,list))
                    if isinstance(v,list):
                         #print(v)
                         for v_list in v:
                              #n += 1
                              #print(n)
                              #print(v_list)
                              new_data[json_k + "_" + k] = v_list
                              #print(new_data)
                              list2.append(new_data.copy())
print(list2)                    
          #new_data[json_k + "_" + k] = v          
print(new_data)
df=pd.DataFrame(list2)
print(df.to_string)
df.to_csv("json_file1.csv",index=False)


## csv file with name as well
new_data = dict()
list2 = []
list1 = []
for json_k,json_v in jsondata.items():
     #print(isinstance(json_v,list))
     if not isinstance(json_v,list):
          new_data[json_k] = json_v
     else:
          #isinstance(json_v,list):
          for i in json_v:
               #print(i)
               for k,v in i.items():
                    #print(isinstance(v,list))
                    if not isinstance(v,list):
                         new_data[json_k + "_" + k] = v
                         list1.append(new_data.copy())
                    else:
                         #isinstance(v,list):
                         #print(v)
                         for v_list in v:
                              #n += 1
                              #print(n)
                              #print(v_list)
                              new_data[json_k + "_" + k] = v_list
                              #print(new_data)
                              list1.append(new_data.copy())
                              
#print(new_data)
print(list1)
print("")
print("")
#print(list2)

     #new_data[json_k + "_" + k] = v          
#print(new_data)
#df=pd.DataFrame(list2)
#print(df.to_string)
#df.to_csv("json_file2.csv",index=False)
