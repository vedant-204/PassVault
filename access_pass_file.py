import mysql.connector
from mysql.connector import errorcode
import pyperclip
def access_my_password(table_name1, x):
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()
    sql = 'select gen_pass from ' + table_name1 + ' where app_name = ' + '"' + x + '"'
    op_cursor.execute(sql)
    verify1 = op_cursor.fetchall()
    if verify1 == []:
        return False
    else:
        verify_list = []
        for _ in verify1:
            verify_list.append(_[0])
        password = verify_list[0]
        return pyperclip.copy(password)