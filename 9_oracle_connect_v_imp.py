import pandas as pd
import cx_Oracle

print(cx_Oracle.version)
##print(cx_Oracle.clientversion())


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

#def extract():
#    try:
# Connect to the database
src_conn = cx_Oracle.connect("system", "sharad123", "LAPTOP-3NEKT69J.broadband:1521/XE")
#create a Cursor
src_cursor = src_conn.cursor()

# Below is dat ain List to insert into table
# Define the data to be inserted
#data = [
#        (1, 'John Doe', 'Male', '01-JAN-2000'),
#        (2, 'Jane Doe', 'Female', '01-JAN-2001'),
#        (3, 'John Smith', 'Male', '01-JAN-2002'),
#        (4, 'Jane Smith', 'Female', '01-JAN-2003')
#        ]
#print (data)
# Execute the INSERT statement using executemany
#table_name = "my_table"
#src_cursor.executemany(f"INSERT INTO {table_name} (id, name, gender, birth_date) VALUES (:1, :2, :3, :4)", data)
#src_conn.commit()

# Close the cursor and connection
#src_cursor.close()

rows_imported = 0
src_tables = "STUDENT"
src_cursor.execute(f"Select * from {src_tables}")
rows = src_cursor.fetchall()        
        
# load data in data frame
df = pd.DataFrame(rows, columns=[i[0] for i in src_cursor.description])
print(df.to_string)
target_table = "STUDENT_DTLS"
#column_list = ",".join(df.columns)  # Get the column names as a comma-separated string
print (df.to_dict("records"))
# NOTE :- in values if we give (:1,:2) we may get error "Data  load error ORA-01036: illegal variable name/number"
#         but if we specify :STUDENT_ID and :NAME it willbe able to know which value should be inserted in which column
src_cursor.executemany(f"Insert into {target_table} (student_id, name) VALUES (:STUDENT_ID, :NAME)", df.to_dict("records"))
#src_cursor.executemany(f"INSERT INTO {target_table} ({column_list}) VALUES ({','.join([':'+str(i+1) for i in range(len(df.columns))])})", df.to_dict("records"))
rows_imported += len(df)
print("NO of rows imported :", rows_imported)
src_conn.commit()
print("Records Commited")
# close sursor
src_cursor.close()
src_conn.close()
