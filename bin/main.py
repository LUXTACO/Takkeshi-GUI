import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
import subprocess
import os
from colored import fg
color = fg('white')

win = tk.Tk()
win.title("Takkeshi GUI")
win.iconbitmap("icon.ico")
win.resizable(False, False)
win.geometry("300x100")
aLabel = ttk.Label(win ,text="Takkeshi GUI" ,font=("Lucon", 16))
aLabel.grid(column=0, row=0)
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=0)
 
mainframe = tk.Frame(win)
mainframe.grid(column=0, row=0, sticky='new')
mainframe.grid_columnconfigure(0, weight=3)

def hwic():
	os.system("python hwic.py")
	print(color + "")
	print("======================================================================================")
	print("")
def stp():
	os.system("python setup.py")
	print(color + "")
	print("======================================================================================")
	print("")
def psg():
	os.system("python psg.py")
	print(color + "")
	print("")
	print("======================================================================================")

action = ttk.Button(win, text="HWIC", command=hwic)
action.grid(column=0, row=1)
action = ttk.Button(win, text="SETUP", command=stp)
action.grid(column=0, row=2)
action = ttk.Button(win, text="PASSGEN", command=psg)
action.grid(column=0, row=3)

win.mainloop()