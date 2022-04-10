import mysql.connector
import os
def store_data():
    curr_d1 = os.getcwd()
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()

    data_log = open('login_data.txt', 'r')
    data_list_auth = []
    with data_log:
        for i in data_log:
            damn = i[:-1]
            data_list_auth.append(damn)
    data_log.close()
    auth_com = "select master_password from master_table"
    op_cursor.execute(auth_com)
    auth1 = op_cursor.fetchall()
    user_com = "select username from master_table"
    op_cursor.execute(user_com)
    auth2 = op_cursor.fetchall()
    auth_list = []
    aut_user_list = []
    for _ in auth1:
        auth_list.append(_[0])
    for j in auth2:
        aut_user_list.append(j[0])
    if len(data_list_auth) == 0:
        pass
    else:
        if data_list_auth[1] in auth_list and data_list_auth[0] in aut_user_list:
            return True
        else:
            return False

store_data()
