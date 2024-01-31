import json

#####
##connection to oracle
# write -- json.dump()
# read  -- json.load()
# update --json.update()

import pandas as pd
import cx_Oracle
print(cx_Oracle.version)

#IMP
#cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library: "The specified module could not be found".
#See https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html for help

#Went on the http site and downloaded
#https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# and placed the "instantclient_21_9" folder in /Users/yashi/Downloads/ directory to make
# cx_Oracle.connect to work (i.e. connect to database to work)
#Later copied to C:\sharad\panda_scripts to check if it works asn left it there, as it works
#IMP
cx_Oracle.init_oracle_client(lib_dir="C:/sharad/panda_scripts/instantclient_21_9")

#conn_str = cx_Oracle.connect('system/sharad123@LAPTOP-3NEKT69J.broadband:1521/XE')
src_conn = cx_Oracle.connect("system", "sharad123", "LAPTOP-3NEKT69J.broadband:1521/XE")
#create a Cursor
cur = src_conn.cursor()

print(src_conn)
######


TABLE_NAME = "tab1"

sqlstatement = ''
with open ('data122.json','r') as f:
    jsondata = json.loads(f.read())

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
    #print (keylist)
    #print(valuelist)
    sqlstatement = "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist +" "
    print(sqlstatement)
    cur.execute(sqlstatement)
    src_conn.commit()
