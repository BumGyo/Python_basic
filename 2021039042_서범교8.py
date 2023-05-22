# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:02:31 2023

@author: 208-PC
"""

sum = 0

for i in range(1, 101) :
    if i%3 == 0 :
        sum = sum + i

print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다." %sum)