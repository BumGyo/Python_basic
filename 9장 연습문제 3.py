# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:39:15 2023

@author: 208-PC
"""

from tkinter import *

win = Tk()

for y in range(0, 10):
    for x in range(0, 3):
        b = Button(win, text=f"{x}행, {y}열").grid(row=x, column=y)
        
win.mainloop()