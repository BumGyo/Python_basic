# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:55:09 2023

@author: 208-PC
"""

matrix = []
count = int(input("리스트 개수를 입력 : "))

for i in range(count) :
    num = int(input("%d번째 데이터 입력 : " %(i+1)))
    matrix.append(num)

for x in range(count) :
    print(matrix[x], ":", "*" * matrix[x])