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

# Connect to the database
connection = cx_Oracle.connect("system", "sharad123", "LAPTOP-3NEKT69J.broadband:1521/XE")

# Create a cursor
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM dual")

# Fetch the results
result = cursor.fetchall()

# Loop through the results and print each row
for row in result:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()



