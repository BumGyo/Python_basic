# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:31:58 2023

@author: 208-PC
"""

coupon = int(input("쿠폰 개수 입력:"))
             
if coupon >= 20 :
	print("\n여행가방")
elif coupon >= 10 :
	print("\n다이어리")
elif coupon < 10 :
	print("\n커피 1잔")