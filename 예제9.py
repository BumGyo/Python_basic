# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:08:57 2023

@author: 208-PC
"""

hot = float(input("온도를 입력하시오: "))

if hot < 0 :
    print("물의 상태는 고체입니다.")
elif 0 <= hot <= 100 :
    print("물의 상태는 액체입니다.")
elif hot > 100 :
    print("물의 상태는 기체입니다.")

