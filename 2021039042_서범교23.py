# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:51:52 2023

@author: 208-PC
"""

# Box Class 정의
class Box :
    def __init__(self, l, h, d):
        self.l = l
        self.h = h
        self.d = d
        
    def __str__(self):
        return "(" + str(self.l) + "," + str(self.h) + "," + str(self.d) + ")"
    
    def getLength(self):
        return self.l
    
    def getHeight(self):
        return self.h
    
    def getDepth(self):
        return self.d
        
b1 = Box(100, 100, 100)
print(b1)
print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())