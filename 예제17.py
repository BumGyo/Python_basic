# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:04:13 2023

@author: 208-PC
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")

def square(length) :
    t.down()
    for i in range(4) :
        t.forward(length)
        t.left(90)
    t.up()

square(100)
t.forward(120)
square(100)
t.forward(120)
square(100)

turtle.mainloop()
turtle.bye()