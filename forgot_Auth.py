import mysql.connector
def givepassword(username_user_auth):
    passdb = mysql.connector.connect(
        host = "sql6.freesqldatabase.com",
        user = "sql6484968",
        passwd = "5k2eTqIMvv",
        database = "sql6484968"
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
