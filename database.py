import mysql.connector
import os
def store_data():
    curr_d2 = os.getcwd()
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()

    data_out = open('signup_data.txt', 'r')
    data_list_out = []
    with data_out:
        for i in data_out:
            damn = i[:-1]
            data_list_out.append(damn)
    sql_data = "insert into master_table (username, email_id, master_password) values (%s, %s, %s)"
    user_rec = tuple(data_list_out)
    
    op_cursor.execute(sql_data, user_rec)
    passdb.commit()

