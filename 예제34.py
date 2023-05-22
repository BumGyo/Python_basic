# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:41:41 2023

@author: 208-PC
"""

from tkinter import *

window = Tk()

Button(window, text="박스 #1", bg="red", fg="white").pack(side=LEFT)
Button(window, text="박스 #2", bg="green", fg="black").pack(side=LEFT)
Button(window, text="박스 #3", bg="orange", fg="white").pack(side=LEFT)

window.mainloop()