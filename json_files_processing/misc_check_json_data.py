import json


with open ('data122.json','r') as f:
    jsondata = json.loads(f.read())

print("")
print(' print file data in single line , NOT easy to read')
print("")
print(jsondata)

print("")
print("")
print(' print file data in readable format, easy to read')
print("")
print(json.dumps(jsondata, indent=4))

for json in jsondata:
    keylist = "("
    valuelist = "("
    firstPair = True
    
    for key, value in json.items():
        if not firstPair:
            keylist += ", "
            valuelist += ", "
        firstPair = False
        keylist += key
        valuelist += "'" + str(value) + "'"
    keylist += ")"
    valuelist += ")"


    print (keylist)
    print (valuelist)
