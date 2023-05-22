# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:54:40 2023

@author: 208-PC
"""

sum = 0

a = int(input("첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))
        
if a < b :
    for l in range(a , b + 1):
        sum += l
    print("%d 부터 %d 까지의 합은 : %d" %(a, b, sum))
      
else :
    for i in range(b , a + 1):
        sum += i
    print("%d 부터 %d 까지의 합은 : %d" %(b, a, sum))