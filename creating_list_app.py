import mysql.connector
def list_apps(table_name2):
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()
    comm = "select app_name from " + str(table_name2)
    op_cursor.execute(comm)
    app_list = op_cursor.fetchall()
    li = []
    for i in app_list:
        m = i[0]
        li.append(m)
    return li