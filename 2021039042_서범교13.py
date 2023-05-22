# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:16:52 2023

@author: 208-PC
"""

score = 0
total = 0

for i in range(1, 6):
    score = int(input("%d번째 성적 입력 : " %i))
    print("%d번째 성적 : %d"  %(i, score))
    total += score
    
print("총점 :", total)
print("평균 :", total / 5)