import json
import pandas as pd


with open ('json_file1.json','r') as f:
    jsondata = json.loads(f.read())

#print(jsondata)
# This to indent the output of json to see how it looks when loaded from file using above loads function
print(json.dumps(jsondata, indent=4))


new_data = dict()
list2 = []
for json_k,json_v in jsondata.items():
     #print (json_k)
     #print (json_v)

     if not isinstance(json_v,list):
          new_data[json_k] = json_v
         # print(new_data)
     else:
          #print(json_v)
          for nested_dict in json_v:
               #print (nested_dict)
               for key,value in nested_dict.items():
                    print(value)
                    if isinstance(value,list):
                         for v in value:
                              new_data[key] = v
                              #print(v)
                              list2.append(new_data.copy())
                    else:
                         new_data[key] = value
                         
               #list2.append(new_data.copy()) # it shuold be here uncommnetd but thi gives duplicate rows so commented   
                    
 
     
#print(new_data)
print("")
print("")
print(list2)

# getting duplicates so code to remove duplicates on the basis of COURSES from list2 (get unique values in list with dictionary value)
#i.e values() + dictionary comprehension
b = {x['courses']:x for x in list2}.values()

print("")
print("")

# create dataframe and load it into csv file
print(b)
df= pd.DataFrame(b)
print(df.to_string)
df.to_csv("json_file3_naturelization_with_code.csv",index=False)   # no indexes in csv file like 0 ,1,2 as we see in output


# duplicates are coming 
#duplicate values
#[{'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'Responsive Web Design', 'courses': 'HTML'},
# {'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'Responsive Web Design', 'courses': 'CSS'},
# {'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'Responsive Web Design', 'courses': 'CSS'},
# {'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'JavaScript Algorithms and Data Structures', 'courses': 'JavaScript'}, {'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'JavaScript Algorithms and Data Structures', 'courses': 'JavaScript'}]

#After removing duplicates

#dict_values([{'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'Responsive Web Design', 'courses': 'HTML'},
#             {'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'Responsive Web Design', 'courses': 'CSS'},
#             {'organization': 'freeCodeCamp', 'website': 'https://www.freecodecamp.org/', 'formed': 2014, 'founder': 'Quincy Larson', 'name': 'JavaScript Algorithms and Data Structures', 'courses': 'JavaScript'}])

