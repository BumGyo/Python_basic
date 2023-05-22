# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:59:54 2023

@author: 208-PC
"""

score = []
count = 0

for i in range(0, 5) :
    score.append(int(input("성적을 입력하시오: ")))
    if score[i] >= 80 :
        count = count + 1

print("성적 평균 = ", sum(score)/len(score))
print("최대 점수 = ", max(score))
print("최소 점수 = ", min(score))
print("80점 이상 = ", count)