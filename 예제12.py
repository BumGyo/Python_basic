# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:59:26 2023

@author: 208-PC
"""

import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오 :")
if s == "사각형" :
    w = int(turtle.textinput("", "가로: "))
    h = int(turtle.textinput("", "세로: "))
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    
if s == "삼각형" :
    while True :
        a = int(turtle.textinput("", "a변: "))
        b = int(turtle.textinput("", "b변: "))
        c = int(turtle.textinput("", "c변: "))
        if (a + b) > c and (b + c) > a and (a + c) > b :
            print("올바른 삼각형")
            break
        else :
            print("삼각형이 만들어지지 않습니다. 다시 입력하세요")
            
    
if s == "원" :
    
turtle.mainloop()
turtle.bye()