# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:42:54 2023

@author: 208-PC
"""

aList = [80, 20, 20, 30, 60, 30]
bList = sorted(set(aList))
print(bList)

student = { 1: {"name": "Kim", "age":"21", "gender":"Female"},
            2: {"name": "Park", "age":"22"}}

cList = {x : x*x for x in range(1, 11)}
print(cList)


myDict = {"옷": 100, "컴퓨터": 2000, "모니터": 320}
print(sum(myDict.values()))

colors = ["red", "green", "blue"]
values = ["#FF0000", "#008000", "#0000FF"]
color_dictionary = dict(zip(colors, values))
print(color_dictionary)

a = set(input("첫 번째 문자열: "))
b = set(input("두 번째 문자열: "))
c = a & b
print("모두 포함된 글자: ", c)