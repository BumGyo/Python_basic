# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:50:04 2023

@author: 208-PC
"""

import math

class Circle:
    def __init__(self, rad):
        self.rad = rad
    
    def getArea(self):
        return math.pi * self.rad**2
    
    def getPrimeter(self):
        return 2 * math.pi * self.rad
    
c = Circle(10)
print("원의 면적", c.getArea())
print("원의 둘레", c.getPrimeter())
    