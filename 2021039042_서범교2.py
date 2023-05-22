# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:33:54 2023

@author: 208-PC
"""

from random import randint

com = randint(1,3)
user = int(input("선택하시오(1:가위, 2:바위, 3:보): "))
if user == com:
    print("비겼습니다!")
elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
    print("user 승!")
elif (user == 1 and com == 2) or (user == 2 and com == 3) or (user == 3 and com == 1):
    print("com 승!")