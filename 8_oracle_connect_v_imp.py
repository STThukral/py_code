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
conn_str = cx_Oracle.connect('system/sharad123@LAPTOP-3NEKT69J.broadband:1521')


df = pd.read_sql("SELECT * FROM student", con=conn_str)
print(df.to_string)

#create a Cursor
src_cursor = conn_str.cursor()

print(df.to_dict("records"))
#to_dict is to chnage the table into dictornary
target_table = "student_dtls"
src_cursor.executemany(f"Insert into {target_table} (student_id, name) VALUES (:STUDENT_ID, :NAME)", df.to_dict("records"))

# inserting records using procedure can be used in seperate script
# just used in same script so that can use src_cursor
#above src_cursor.executemany also inserts in student_dtls and
# below oracle procedure is another way to insert records.
#student_class_ins is procedure created in oracle but called in python
# to insert records in student_dtls and class_dtls
print("Inserting using Procedure")
out_var1=src_cursor.var(int)
out_var2=src_cursor.var(int)
src_cursor.callproc('student_class_ins',(out_var1,out_var2))
# similarly we can callfunc as well to call oracle function pandas script
print("No of student records inserted :: " + str(out_var1.getvalue()))
print("No of class records inserted :: " + str(out_var2.getvalue()))

print("Inserting using Procedure end")

conn_str.commit()
conn_str.close()
