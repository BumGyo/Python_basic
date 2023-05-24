# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:30:46 2023

@author: 208-PC
"""

from tkinter import *

def clicked():
    pass

window = Tk()

myButton = Button(window, text="Click me", command=clicked).pack()

window.mainloop()