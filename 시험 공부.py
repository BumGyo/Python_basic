# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:13:19 2023

@author: 208-PC
"""

bmi = 23.5556634643
print("%0.2f" %bmi)

result = 0

for i in range(2, 100, 2) :
    result += i
    print(i)

for y in range(1, 4):
    for x in range(y) :
        x += 1
        print(x, end ="")
        
    print("")
    
num = 1
for i in range(1, 4):    # 3번 반복
    for j in range(i):   # i번 반복
        if num > 6:      # num이 6을 넘으면 break
            break
        print(num, end="")
        num += 1
    print()    