from tkinter import *
from tkinter import ttk
import time
root = Tk()
def star_prog():
    for i in range(10):
        progress_bar['value'] += 10
        root.update_idletasks()
        time.sleep(1)
frame = Frame(root)
frame.grid()
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='blue')
progress_bar = ttk.Progressbar(frame, style="red.Horizontal.TProgressbar", orient="horizontal", length=600, mode="determinate", maximum=4, value=1)
progress_bar.pack()
prog_button = Button(frame,text = "press", command = star_prog)
prog_button.pack()
frame.pack()


root.mainloop()