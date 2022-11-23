from cgitb import text
import tkinter
from tkinter.tix import Tk
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

#call win the main window plus title plux size
win = Tk()
win.title('Welcome')
win.geometry('700x400')

#icon file path
p1 = PhotoImage(file =r'')   
# Icon set for program window
win.iconphoto(False, p1)   

#choose file 
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
#create button for browsefiles
button_explore = Button(win,
                        text = "Browse Files",
                        width=14,height=4,
                        command = browseFiles)
#exit button
button_exit = Button(win,
                     text = "Exit",
                     width=4,height=2,
                     command = exit)
#header
lab = Label(win, text="Automation Hub", anchor=CENTER)
#buttons position
button_explore.grid(column=2,row=2,padx=305,pady=20)

lab.grid(column=2,row=0,padx=305,pady=15)
  
button_exit.grid(column=2,row=3,padx=305,pady=10)

#test
def func() :
    tkinter.messagebox.showinfo("hey", "hello")

#button for test
btn = Button(win, text="Start", width=10,height=6,command=func)
btn.grid(column=2,row=1,padx=305,pady=10)

#no resizeing fn
win.resizable(False, False) 
#starts here
win.mainloop()

