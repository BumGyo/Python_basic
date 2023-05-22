# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:00:43 2023

@author: 208-PC
"""

class Rocket :
    def __init__(self) :
        self.x = 0
        self.y = 0
    
    def __str__() :
        pass
        
    def moveUp(self) :
        self.y += 1
        
myRocket = Rocket()
print("로켓의 높이 :", myRocket.y)

myRocket.moveUp()
print("로켓의 높이 :", myRocket.y)