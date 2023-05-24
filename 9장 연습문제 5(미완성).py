# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:45:55 2023

@author: 208-PC
"""

from tkinter import *

win = Tk()

def increase():
    count += 1
    
def decrease():
    count -= 1


d = Button(win, text="감소", command=decrease).grid(row=0, column=0)
l = Label(win, text=count).grid(row=0, column=1)
i = Button(win, text="증가", command=increase).grid(row=0, column=2)

win.mainloop()