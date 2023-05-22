# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:04:41 2023

@author: 208-PC
"""

def calc(var1, var2, oper):
    if oper == "+":
        return var1 + var2
    elif oper == "-":
        return var1 - var2
    elif oper == "*":
        return var1 * var2
    elif oper == "/":
        return var1 / var2
    else :
        print("다시 입력하세요")
        return 0


# main 코드
oper = input("게산을 입력하세요(+, -, *, /) :")
var1 = int(input("첫 번째 수를 입력하세요 : "))
var2 = int(input("첫 번째 수를 입력하세요 : "))

result = calc(var1, var2, oper)

print("## 계산기 : %d %s %d = %d" %(var1, oper, var2, result))