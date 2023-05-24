# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:59:25 2023

@author: 208-PC
"""

from tkinter import *

window = Tk()

def key(event):
    print( repr(event.char), "가 눌렸습니다.")
    
def callback(event) :
    frame.focus_set()
    print(event.x, event.y, "에서 이벤트 발생")

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()