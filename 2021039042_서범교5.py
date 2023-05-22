# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:28:17 2023

@author: 208-PC
"""

num = int(input("단을 입력하세요 : "))

for i in range(1, 10) :
    print("%d X %d = %2d" %(num, i, num*i))