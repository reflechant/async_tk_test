#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trying to create an async app with Tk. Main module
"""

from sys import version
if version.split()[0][0] == '2':
    import Tkinter as tk
    import Queue as Q
elif version.split()[0][0] == '3':
    import tkinter as tk
    import queue as Q
else:
    print "Невозможно определить установленную версию интерпретатора Python"
    exit()

import string

