import mysql.connector
def list_apps(table_name2):
    passdb = mysql.connector.connect(
        host = "sql6.freesqldatabase.com",
        user = "sql6484968",
        passwd = "5k2eTqIMvv",
        database = "sql6484968"
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
