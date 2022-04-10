from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import encryption
import decryption
from cryptography.fernet import Fernet
import pickle
import database
import ctypes
import auth
import user_table
import password_generator
import random,string
import access_pass_file
import smtplib
import creating_list_app
import forgot_pass_comm
import forgot_Auth

#functions
def forgot_password():
    forgot_frame.tkraise()
def login():
    login_input = open('login_data.txt', 'w')
    data_log = [user_entry.get(), pass_entry.get()]
    with login_input:
        for i in data_log:
            login_input.write('%s\n' % i)
    login_input.close()
    if auth.store_data() == True:
        user_window_frame.tkraise()
        Label(user_window_frame, text = ("Hi", str(user_entry.get())), font = ("Bahnschrift Light Condensed",23,"bold"), fg = "#D1E1FF", bg = "#364B71").place(x = 65, y = 75)
    else:
        auth_denial = Label(login_frame, text = "Please check your password/username or sign up!", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
        auth_denial.place(x = 73, y = 370)
def Signup():
    signup_frame.tkraise()
def sign_user():
    input_file = open('signup_data.txt', 'w')
    data_list = [user_entry2.get(), email_entry.get(), pass_entry2.get()]
    with input_file:
        for i in data_list:
            input_file.write('%s\n' % i)
        input_file.close()
    if user_table.verify_signup() == False:
        signup_denial = Label(signup_frame, text = "You are already registered!", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
        signup_denial.place(x = 53, y = 380)
        user_entry2.delete(0,END)
        email_entry.delete(0,END)
        pass_entry2.delete(0,END)
        Name_entry.delete(0,END)
        user_entry2.focus()
    else:
        database.store_data()
        #li = [email_entry.get()] 
        #for dest in li:
        #    s = smtplib.SMTP('smtp.gmail.com', 587) 
        #    s.starttls() 
        #    s.login("passvault.storepasses@gmail.com", "storingpasswordshere") 
       #     message = "Thank you for registering in PassVault."
      #      s.sendmail("passvault.storepasses@gmail.com", dest, message) 
     #       s.quit() 
        login_frame.tkraise()
    input_file.close()
    input_file = open('signup_data.txt', 'r+')
    input_file.truncate(0)
    input_file.close()
def giveawaypass():
    if forgot_Auth.givepassword(username_user_auth = user_forg_name_entry.get()) == False:
        Label(forgot_frame, text = "Enter correct Username", font = ("Bahnschrift Light Condensed",10,"bold"), fg = "#D1E1FF", bg = "#364B71").place(x = 33, y = 250)
    else:
        forgot_pass_comm.iforgotpasses(username_user = user_forg_name_entry.get())
        ctypes.windll.user32.MessageBoxW(0, "Password successfully mailed", "Confirmation", 1)
        login_frame.tkraise()

def access_pass():
    def back_butt1():
        top3.destroy()
    def access_frm_database(entry):
        access_pass_file.access_my_password(table_name1 = user_entry.get(), x = app_name_menu.get())
        ctypes.windll.user32.MessageBoxW(0, "Password is Copied to your clipboard", "Confirmation", 1)
        top3.destroy()
        
    main_app_li = creating_list_app.list_apps(table_name2 = user_entry.get())
    top3 = Toplevel(root)
    top3.geometry ("754x504")
    top3.title("PassGen")
    #top3.iconbitmap(r'icon.ico')
    top3.resizable(0,0)

    back_img4 = Image.open('w1.png') 
    Logo_img1 = Image.open('logo.png')
        
    back_gg1 = ImageTk.PhotoImage(back_img4)
    logo1 = ImageTk.PhotoImage(Logo_img1)
        
    background4 = Label(top3, image = back_gg1)
    acc_pass_frame = Frame(top3, bg = "#364B71")
        
    Logo_label4 = Label(top3, image = logo1, bg = "#364B71")   
    intro1_label2 = Label(acc_pass_frame, text = "Access your password", font = ("Bahnschrift Light Condensed",23,"bold"), fg = "#D1E1FF", bg = "#364B71")
    app_name_label1 = Label(acc_pass_frame, text = "Enter name of application", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
    app_name_menu = ttk.Combobox(acc_pass_frame, value = main_app_li)
    app_name_menu.current(0)
    app_name_menu.bind("<<ComboboxSelected>>",access_frm_database)
    back_out1 = Button(top3, text = "Back", font =  ("Bahnschrift Light Condensed", 10), bd = 1, bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = back_butt1)

        
    background4.place(x = 0,y = 0)
    Logo_label4.place(x = 225, y = 22, height = 50, width = 50)
    acc_pass_frame.place(x = 50, y = 50, height = 400, width = 400)
    intro1_label2.place(x = 40, y = 30)
    app_name_label1.place(x = 33, y = 110)
    app_name_menu.place(x = 33, y = 135, height = 30, width = 325)
    back_out1.place(x = 693, y = 5, height = 25, width = 55)
        
    top3.mainloop()

def generating_pass():
    print(user_entry.get())
    gen_pass_frame.tkraise()
def logout():
    login_frame.tkraise()
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    user_entry.focus()
def pass_to_database():
    imp_file = open('generating_passes.txt', 'w')
    pass_list = [app_name_entry.get(), app_user_name_entry.get()]
    with imp_file:
        for i in pass_list:
            imp_file.write('%s\n' % i)
    imp_file.close()
    passdb = mysql.connector.connect(host = "localhost", user = "root", passwd = "1234", database = "password_manager")
    op_cursor = passdb.cursor()
    pass_log = open('generating_passes.txt', 'r')
    pass_list = []
    with pass_log:
        for i in pass_log:
            q = i[:-1]
            pass_list.append(q)
    pass_log.close()
    pass_list.append(password_generator.generate_pass())
    table_name = user_entry.get()
    pass_tup = tuple(pass_list)
    pass_insert_comm = 'insert into ' + table_name + ' (app_name, username_app, gen_pass) VALUES '
    command = pass_insert_comm + str(pass_tup)
    op_cursor.execute(command)
    passdb.commit()
    imp_file = open('generating_passes.txt', 'r+')
    imp_file.truncate(0)
    imp_file.close()
    app_name_entry.delete(0, END)
    app_user_name_entry.delete(0, END)
    app_name_entry.focus()
    
def back_butt():
    user_window_frame.tkraise()

def back_butt2():
    login_frame.tkraise()

root = Tk()

#root intials
root.geometry ("754x504")
root.title("PassVault")
#root.iconbitmap(r'icon.ico')
root.resizable(0,0)

#root settings
back_img = Image.open('w1.png')
signup_img = PhotoImage(file = 'signup.png')
Logo_img = Image.open('logo.png')
back = ImageTk.PhotoImage(back_img)
logo = ImageTk.PhotoImage(Logo_img)
Label(root, image = back).place(x = 0, y = 0)
Label(root, image = logo, bg = "#364B71").place(x = 225, y = 22, height = 50, width = 50)

#frames used
login_frame = Frame(root, bg = "#364B71")
signup_frame = Frame(root, bg = "#364B71")
forgot_frame = Frame(root, bg = "#364B71")
gen_pass_frame = Frame(root, bg = "#364B71")
access_pass_frame = Frame(root, bg = "#364B71")
user_window_frame = Frame(root, bg = "#364B71")

frame_tup = (login_frame, signup_frame, forgot_frame, gen_pass_frame, access_pass_frame, user_window_frame)

#putting frames in root
for frames in frame_tup:
    frames.place(x = 50, y = 65, height = 400, width = 400)

#imp_variables


#login_frame
user_label = Label(login_frame, text = "Username", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
pass_label = Label(login_frame, text = "Enter Master Password", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
user_entry = Entry(login_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
pass_entry = Entry(login_frame, show = "*", borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
intro_label = Label(login_frame, text = "PassVault"+chr(169), font = ("Bahnschrift Light Condensed",30,"bold"), fg = "#D1E1FF", bg = "#364B71")
ask = Label(login_frame, text = "Not registered yet ?", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
login_button = Button(login_frame, text = "LOGIN", font = ("Bahnschrift Light Condensed",15), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = login)
signup_button = Button(login_frame, text = "CREATE AN ACCOUNT", font = ("Bahnschrift Light Condensed",10), bd = 0, bg = "#364B71", activebackground = "#364B71", cursor = "hand2", fg = "#D1E1FF", command = Signup)
forgot_pass = Button(login_frame, text = "- Forgot Password ? -", font = ("Bahnschrift Light Condensed",10), bd = 0, bg = "#364B71", activebackground = "#364B71", cursor = "hand2", fg = "#D1E1FF", command = forgot_password)

intro_label.place(x = 100, y = 30 )
user_label.place(x = 33, y = 90)
user_entry.place(x = 33, y = 115, height = 30, width = 325)
pass_label.place(x = 33, y = 150)
pass_entry.place(x = 33, y = 175, height = 30, width = 325)
login_button.place(x = 33, y = 220, height = 60, width = 325)
ask.place(x = 73, y = 293)
signup_button.place(x = 197, y = 293)
forgot_pass.place(x = 135, y = 310)

#signup_frame
user_label2 = Label(signup_frame, text = "Username", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
email_label = Label(signup_frame, text = "Email id", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
Name_label = Label(signup_frame, text = "Enter your Name", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
pass_label2 = Label(signup_frame, text = "Enter Master Password", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
user_entry2 = Entry(signup_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
email_entry = Entry(signup_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
Name_entry = Entry(signup_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
pass_entry2 = Entry(signup_frame, show = "*", borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
intro_label2 = Label(signup_frame, text = "Welcome to PassVault", font = ("Bahnschrift Light Condensed",23,"bold"), fg = "#D1E1FF", bg = "#364B71")    
signup_button2 = Button(signup_frame, text = "SIGN UP", font = ("Bahnschrift Light Condensed",15), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = sign_user)
back_out2 = Button(signup_frame, text = "< Back", font =  ("Bahnschrift Light Condensed", 10), bd = 0, bg = "#364B71", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = back_butt2)

back_out2.place(x = 33, y = 10)
intro_label2.place(x = 30, y = 30 )
user_label2.place(x = 33, y = 90)
user_entry2.place(x = 33, y = 115, height = 30, width = 325)
email_label.place(x = 33, y = 150)
email_entry.place(x = 33, y = 175, height = 30, width = 325)
Name_label.place(x = 33, y = 210)
Name_entry.place(x = 33, y = 235, height = 30, width = 325)
pass_label2.place(x = 33, y = 270)
pass_entry2.place(x = 33, y = 295, height = 30, width = 325)
signup_button2.place(x = 33, y = 335, height = 40, width = 325)

#forgot_frame
forg1_label = Label(forgot_frame, text = "Forgot Password", font = ("Bahnschrift Light Condensed",23,"bold"), fg = "#D1E1FF", bg = "#364B71")
user_forg_name_label = Label(forgot_frame, text = "Enter registered username", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
user_forg_name_entry = Entry(forgot_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
forg_pass1 = Button(forgot_frame, text = "Get Password", font = ("Bahnschrift Light Condensed",15), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = giveawaypass)
back_out3 = Button(forgot_frame, text = "< Back", font =  ("Bahnschrift Light Condensed", 10), bd = 0, bg = "#364B71", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = back_butt2)

forg1_label.place(x = 44, y = 30)
user_forg_name_label.place(x = 33, y = 110)
user_forg_name_entry.place(x = 33, y = 137, height = 30, width = 325)
back_out3.place(x = 33, y = 350)
forg_pass1.place(x = 33, y = 300, height = 40, width = 325)

#user_win_frame
access_pass = Button(user_window_frame, text = "Access Passwords", font = ("Bahnschrift Light Condensed",15), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = access_pass)
gen_pass = Button(user_window_frame, text = "Generate Passwords", font = ("Bahnschrift Light Condensed",15), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = generating_pass)
log_out = Button(user_window_frame, text = "Log Out", font =  ("Bahnschrift Light Condensed", 10),bd = 0 ,bg = "#364B71", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = logout)

access_pass.place(x = 33, y = 250, height = 60, width = 325)
gen_pass.place(x = 33, y = 150, height = 60, width = 325)
log_out.place(x = 33, y = 350, height = 25, width = 55)

#gen_pass_frame
intro1_label = Label(gen_pass_frame, text = "Details for PassGen", font = ("Bahnschrift Light Condensed",23,"bold"), fg = "#D1E1FF", bg = "#364B71")
app_name_label = Label(gen_pass_frame, text = "Enter name of application", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
app_name_entry = Entry(gen_pass_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
app_user_name_label = Label(gen_pass_frame, text = "Enter username used for app", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
app_user_name_entry = Entry(gen_pass_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
gen_pass1 = Button(gen_pass_frame, text = "+", font = ("Bahnschrift Light Condensed",30), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = pass_to_database)
back_out = Button(gen_pass_frame, text = "< Back", font =  ("Bahnschrift Light Condensed", 10), bd = 0, bg = "#364B71", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = back_butt)

intro1_label.place(x = 44, y = 30)
app_name_label.place(x = 33, y = 90)
app_name_entry.place(x = 33, y = 115, height = 30, width = 325)
app_user_name_label.place(x = 33, y = 170)
app_user_name_entry.place(x = 33, y = 195, height = 30, width = 325)
gen_pass1.place(x = 33, y = 235, height = 60, width = 325)
back_out.place(x = 33, y = 350, height = 25, width = 55)

login_frame.tkraise()

root.mainloop()
# cN!hn\Gj6~V0L|rJ
