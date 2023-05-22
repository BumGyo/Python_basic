# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:29:22 2023

@author: 208-PC
"""

def circle_area(r) :
    area = r**2*3.14
    return area

r = int(input("반지름 입력 하세요 : "))
area = circle_area(r)
print("반지름이 %d인 원의 면적=" %r , area)