# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:31:07 2023

@author: 208-PC
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)

while True:
    command =input("명령을 입혁하시오")
    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "r":
        t.right(90)
        t.forward(100)
    if command == "q":
        break

turtle.mainloop()
turtle.bye()