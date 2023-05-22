# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:41:49 2023

@author: 208-PC
"""

sum = 0

for i in range(3333, 10000):
    if i % 1234 == 0 :
        continue
    if sum + i > 100000 :
        break
    sum += i

print("실행 결과 : ", sum)