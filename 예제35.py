# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:50:45 2023

@author: 208-PC
"""

from tkinter import *

window = Tk()
window.geometry("600x100")

Button(window, text="박스 #1", width=10, height=1).pack()
Button(window, text="박스 #2", width=10, height=1).pack()
Button(window, text="박스 #3", width=10, height=1).pack()

window.mainloop()