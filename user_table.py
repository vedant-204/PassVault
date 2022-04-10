import mysql.connector
import os
def verify_signup():
    curr_d3 = os.getcwd()
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()

    data_user = open('signup_data.txt', 'r')
    data_list_user = []
    with data_user:
        for i in data_user:
            damn = i[:-1]
            data_list_user.append(damn)
    data_user.close()
    verify_com = "select username, master_password from master_table"
    op_cursor.execute(verify_com)
    verify1 = op_cursor.fetchall()
    verify_list = []
    verify_list_username = []
    for _ in verify1:
        verify_list.append(_[1])
    for i in verify1:
        verify_list_username.append(i[0])
    if data_list_user[2] in verify_list or data_list_user[0] in verify_list_username:
        return False 
    else:
        s = data_list_user[0]
        create_user_comm = "create table %s (app_name varchar(100), username_app varchar(100), gen_pass varchar(765) unique key, ussid integer auto_increment primary key)"%(s)
        op_cursor.execute(create_user_comm)
        passdb.commit()
        