# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:04:59 2023

@author: 208-PC
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = []

print("원래 행렬 = ", matrix)

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix :
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("전치 행렬 = ", transposed)

