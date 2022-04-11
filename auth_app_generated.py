import mysql.connector
from mysql.connector import errorcode
import pyperclip
def wether_generated(table_name3):
    passdb = mysql.connector.connect(
        host = "sql6.freesqldatabase.com",
        user = "sql6484968",
        passwd = "5k2eTqIMvv",
        database = "sql6484968"
        )
    op_cursor = passdb.cursor()
    comm = "select ussid from " + table_name3
    op_cursor.execute(comm)
    dd = op_cursor.fetchall()
    if dd == []:
        return True
    else:
        return False
print(wether_generated('vedant'))
