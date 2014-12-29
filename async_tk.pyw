#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trying to create an async app with Tk. Main module
"""

import sys
import select

#check Python version:
if sys.version.split()[0][0] == '2':
    import Tkinter as tk
elif sys.version.split()[0][0] == '3':
    import tkinter as tk
else:
    print "Невозможно определить установленную версию интерпретатора Python"
    exit()
#---------------------


"""def read():
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line:
            S.set(line)
            root.update_idletasks()
        else:
            #S.set("")
            pass
    else:
        pass
    #root.after(1,read)"""


def shift_lbl(event):
    a = S2.get()
    a = a[-1] + a[:-1]
    S2.set(a)

root = tk.Tk()

S = tk.StringVar()
S.set("TEXT")

S2 = tk.StringVar()
S2.set("TEXT")

L = tk.Label(root, textvariable=S, width=50, height=3)
L.pack()

L2 = tk.Label(root, textvariable=S2)
L2.pack()

B = tk.Button(root, text = "НАЖМИ МЕНЯ")
B.pack()
B.bind("<Button-1>", shift_lbl)

#root.after(1,read)

f = open("tmp")
while True:
    #x = input()
    #x = "TEST TEXT"
    x = f.readline()
    if x:
        S.set(x)
    else:
        f.close()
    root.update()

root.mainloop()
