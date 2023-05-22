# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:01:10 2023

@author: 208-PC
"""

s = input("문자열을 입력하세요 : ")

s1 = s[::-1]

if s == s1 :
    print("회문입니다.")
else :
    print("회문이 아닙니다.")