import pandas as pd
#from connection_class_10 import ST_Oracle_Connection
from connection_class_10 import ST1_Oracle_Connection

#conenction without try and exception
#con = ST_Oracle_Connection()
# connection with try ,exception
con = ST1_Oracle_Connection()
cur = con.cursor()

cur.execute("select count(*) from student_dtls")
#####This uses the fetchone() method to return just a single row as a tuple.
#When called multiple time, consecutive rows are returned:
#####The fetchmany() method returns a list of tuples. By default the number of rows returned
#is specified by the cursor attribute arraysize (which defaults to 100)
count, = cur.fetchone()
print("Number of rows in student_dtls:", count)

rows_imported = 0
src_tables = "STUDENT"
cur.execute(f"Select * from {src_tables}")
rows = cur.fetchall()        
        
# load data in data frame
df = pd.DataFrame(rows, columns=[i[0] for i in cur.description])
print(df.to_string)
target_table = "STUDENT_DTLS"
print (df.to_dict("records"))
# NOTE :- in values if we give (:1,:2) we may get error "Data  load error ORA-01036: illegal variable name/number"
#         but if we specify :STUDENT_ID and :NAME it willbe able to know which value should be inserted in which column
cur.executemany(f"Insert into {target_table} (student_id, name) VALUES (:STUDENT_ID, :NAME)", df.to_dict("records"))

rows_imported += len(df)
print("NO of rows imported :", rows_imported)
con.commit()
print("Records Commited")
# close sursor
cur.close()
con.close()

