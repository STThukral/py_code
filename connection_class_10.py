import pandas as pd
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="C:/sharad/panda_scripts/instantclient_21_9")

class ST_Oracle_Connection(cx_Oracle.Connection):
    def __init__(self):
        print("Connecting to database ST_Oracle_Connection")
        return super(ST_Oracle_Connection, self).__init__("system", "sharad123", "LAPTOP-3NEKT69J.broadband:1521/XE")

# another call with try and excption
# Remove one charater form password to see what kind of error we get
# and we got :-
#Connecting to database ST1_Oracle_Connection
#There is an error in Oracle database :  ORA-01017: invalid username/password; logon denied
class ST1_Oracle_Connection(cx_Oracle.Connection):
    def __init__(self):
        try:
            print("Connecting to database ST1_Oracle_Connection")
            return super(ST1_Oracle_Connection, self).__init__("system", "sharad123", "LAPTOP-3NEKT69J.broadband:1521/XE")
        except cx_Oracle.DatabaseError as er:
            print('There is an error in Oracle database : ', er)
        except Exception as er:
            print('Error :' +str(er))
