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

S = tk.StringVar()
S.set("")

def read():
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line:
            S.set(line)
        else:
            S.set("")
    else:
        pass
    root.after(1,read)

root = tk.Tk()

L = tk.Label(root, textvariable=S)
L.pack()

root.after(1,read)
root.mainloop()
