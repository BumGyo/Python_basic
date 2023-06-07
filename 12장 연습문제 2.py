# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:40:06 2023

@author: 208-PC
"""

class X:
    def __init__(self, a):
        self.a = a
        
class Y(X):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

obj = Y(10, 20)
print(obj.a)