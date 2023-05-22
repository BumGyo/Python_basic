# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:49:31 2023

@author: 208-PC
"""

import random

def dice_game():
    print("========= dice_game()호출 ===========")
    human_num = random.randint(1, 6)
    com_num = random.randint(1, 6)
    print("인간 : 주사위값=", human_num)
    print("컴퓨터 : 주사위값=", com_num)
    if human_num > com_num :
        print("인간승리")
    elif human_num < com_num :
        print("컴퓨터승리")
    else :
        print("무승부")
    print("========= dice_game()복귀 ===========")

while True :
    dice_game()
    tf = input("중단할까요? Y/N")
    if tf == "Y" or tf == "y" :
        break
    else :
        continue
