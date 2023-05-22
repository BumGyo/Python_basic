# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:46:54 2023

@author: 208-PC
"""

class MyClass:
    def __init__(self, a = "Good Morning"):
        self.a = a
        
    def display(self):
        print(self.a)
        
obj = MyClass()
obj.display()