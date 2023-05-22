# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:48:46 2023

@author: 208-PC
"""

weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))
BMI = weight / (height**2)

print("당신의 BMI =", BMI)