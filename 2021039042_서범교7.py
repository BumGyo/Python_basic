# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:01:24 2023

@author: 208-PC
"""

for dan in range(2, 10) :
    print("## %d단 ##" %dan)
    for num in range(1, 10) :
        print("%d X %d = %d" %(dan, num, dan * num))
    print("")