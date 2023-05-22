# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:57:55 2023

@author: 208-PC
"""

import turtle

def draw_thing(some_turtle, tasks) :
    for value in tasks :
        some_turtle.forward(value)
        some_turtle.stamp()
        some_turtle.backward(value)
        some_turtle.right(30)
    
window = turtle.Screen()
bob = turtle.Turtle()

my_list = [10, 20 ,30, 40, 50, 60, 70, 80, 90, 100]
draw_thing(bob, my_list)
turtle.mainloop()
turtle.bye()