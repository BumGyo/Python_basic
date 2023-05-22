# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import turtle
t = turtle.Turtle()
t.shape("turtle")

side = int(input("side 값을 입력하시오: "))
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)

turtle.mainloop()
turtle.bye()