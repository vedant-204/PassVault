from tkinter import *
from tkinter import ttk
root = Tk()
def f(event):
    am = Label(root, text = Drop_Menu.get()).pack()
li = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
goof = StringVar(root)
Drop_Menu = ttk.Combobox(root, value = li) 
Drop_Menu.current(0)
Drop_Menu.bind("<<ComboboxSelected>>", f)
Drop_Menu.pack()
root.mainloop()
