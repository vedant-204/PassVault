def back_butt():
            top2.destroy()
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

        top2 = Toplevel(root)
        top2.geometry ("754x504")
        top2.title("PassGen")
        top2.iconbitmap(r'icon.ico')
        top2.resizable(0,0)
        
        back_img3 = Image.open('w1.png') 
        Logo_img = Image.open('logo.png')
        
        back_gg1 = ImageTk.PhotoImage(back_img3)
        logo = ImageTk.PhotoImage(Logo_img)
        

        background3 = Label(top2, image = back_gg1)
        
        gen_pass_frame = Frame(top2, bg = "#364B71")
        
        Logo_label3 = Label(top2, image = logo, bg = "#364B71")   
        intro1_label = Label(gen_pass_frame, text = "Details for PassGen", font = ("Bahnschrift Light Condensed",23,"bold"), fg = "#D1E1FF", bg = "#364B71")
        app_name_label = Label(gen_pass_frame, text = "Enter name of application", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
        app_name_entry = Entry(gen_pass_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
        app_user_name_label = Label(gen_pass_frame, text = "Enter username used for app", font = ("Bahnschrift Light Condensed",10), bg = "#364B71" , fg = "#D1E1FF")
        app_user_name_entry = Entry(gen_pass_frame, borderwidth = 3, font = ("Bahnschrift Light Condensed",13))
        gen_pass1 = Button(gen_pass_frame, text = "+", font = ("Bahnschrift Light Condensed",30), bd = 1,bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = pass_to_database)
        back_out = Button(top2, text = "Back", font =  ("Bahnschrift Light Condensed", 10), bd = 1, bg = "#4472C4", activebackground = "#364B71", cursor = "hand2", fg = "#FFFFFF", command = back_butt)
        
        background3.place(x = 0,y = 0)
        Logo_label3.place(x = 225, y = 22, height = 50, width = 50)
        gen_pass_frame.place(x = 50, y = 50, height = 400, width = 400)
        intro1_label.place(x = 44, y = 30)
        app_name_label.place(x = 33, y = 90)
        app_name_entry.place(x = 33, y = 115, height = 30, width = 325)
        app_user_name_label.place(x = 33, y = 170)
        app_user_name_entry.place(x = 33, y = 195, height = 30, width = 325)
        gen_pass1.place(x = 33, y = 335, height = 60, width = 325)
        back_out.place(x = 693, y = 5, height = 25, width = 55)
        
        top2.mainloop()