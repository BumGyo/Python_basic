# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:41:22 2023

@author: 208-PC
"""

import turtle
import random

# shapeList에 현재 사용 가능한 모든 거북이 모양의 이름 리스트를 저장한다.
shapeList = turtle.getshapes()
# 0부터 99까지 반복한다.
for i in range(0, 100) :
    # random 모듈을 사용하여 shapeList의 리스트 멤버를 섞어준다.
    random.shuffle(shapeList)
    myTurtle = turtle.Turtle(shapeList[0])
    tX = random.randrange(-swidth / 2, swidth /2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r = random.random(); g = random.random(); b = random.random()
    tSize = random.randrange(1, 3)
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
    
    for tList in playerTurtles :
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])
        
    turtle.done()