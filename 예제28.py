# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:29:16 2023

@author: 208-PC
"""

class Counter:
    def __init__(self, initValue = 0):
        self.count = initValue
    
    def increment(self):
        self.count += 1

a = Counter(0)
a = Counter(100)