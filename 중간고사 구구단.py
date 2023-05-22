# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:03:09 2023

@author: 208-PC
"""

for x in range(2, 10):
    print("## %d단 ##" %x)
    for y in range(1, 10):
        print("%d x %d = %d" %(x, y, x*y))
    print("")