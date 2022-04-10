import mysql.connector
def givepassword(username_user_auth):
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()
    forgot_comm = "select username from master_table"
    op_cursor.execute(forgot_comm)
    ok = op_cursor.fetchall()
    this_li = []
    for j in ok:
        this_li.append(j[0])
    if username_user_auth in this_li:
        return True
    else:
        return False
