# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:03:32 2023

@author: 208-PC
"""

print("1~100사이의 수 중에서 2의 배수이면서 3의 배수가 아닌 수 : ", end=" ")

for i in range(1,101) :
    if (i % 2 == 0 and i % 3 != 0):
        print(i, end =",")
        