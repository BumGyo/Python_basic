# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:20:59 2023

@author: 208-PC
"""

aa = []

for i in range(0, 4) :
    aa.append(0)

hap = 0

for i in range(0, 4) :
    aa[i] = int(input(str(i + 1) + "번째 숫자 : "))
    
for i in range(0, 4) :
    hap += aa[i]
    
print("합계 ==> %d" %hap)