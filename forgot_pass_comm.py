import mysql.connector
import smtplib

def iforgotpasses(username_user):
    passdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "password_manager"
        )
    op_cursor = passdb.cursor()
    forgot_command = "select master_password, email_id from master_table where username = " + "'" + str(username_user) + "'"
    op_cursor.execute(forgot_command)
    password_got = op_cursor.fetchone()
    password_is = []
    for i in password_got:
        password_is.append(i) 
    li = [password_is[1]]
    for dest in li:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("passvault.storepasses@gmail.com", "storingpasswordshere") 
        message = "Your master password for PassVault is " + "'" + str(password_is[0]) + "'" + " ." + " Thank you for using PassVault."
        s.sendmail("passvault.storepasses@gmail.com", dest, message) 
        s.quit()
    return password_is[0]