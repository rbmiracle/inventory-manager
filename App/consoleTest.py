from tkinter import *
from os import system as cmd

root = Tk()
termf = Frame(root, height=800, width=1000)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
cmd('xterm -into %d -geometry 160x50 -sb &' % wid)

root.mainloop()