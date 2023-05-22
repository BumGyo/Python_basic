# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:42:21 2023

@author: 208-PC
"""
price = int(input("상품의 가격: "))

if price > 20000 :
    shipping_cost = 0
else :
    shipping_cost = 3000
    
print("배송비 = ", shipping_cost)
