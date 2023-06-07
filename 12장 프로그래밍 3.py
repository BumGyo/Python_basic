# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:00:07 2023

@author: 208-PC
"""

class Function():
    def __init__(self):
        pass
    def value(self):
        pass
        
class Quadratic(Function):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_roots(self):
        global fx1, fx2
        fx1 = (-self.b + (self.b**2 - 4*self.a*self.c)**(1/2)) / (2 * self.a)
        fx2 = (-self.b - (self.b**2 - 4*self.a*self.c)**(1/2)) / (2 * self.a)
        print(f'solution: {fx1}, {fx2}')
    
    def value(self):
        return self.fx1, self.fx2
    
a = Quadratic(1, 2, 3)
a.get_roots()
a.value()