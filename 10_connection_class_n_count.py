import pandas as pd
import cx_Oracle


class MyConnection(cx_Oracle.Connection):
    cx_Oracle.init_oracle_client(lib_dir="C:/sharad/panda_scripts/instantclient_21_9")

    def __init__(self):
        print("Connecting to database")
        return super(MyConnection, self).__init__("system", "sharad123", "LAPTOP-3NEKT69J.broadband:1521/XE")

con = MyConnection()
cur = con.cursor()

cur.execute("select count(*) from student")
count, = cur.fetchone()
print("Number of rows:", count)
