# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:30:18 2023

@author: 208-PC
"""

num = int(input("정수를 입력하시오: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()