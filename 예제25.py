# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:32:19 2023

@author: 208-PC
"""

myset = {"Milk", "Orange", "Bread"}
myset.add("Butter")
myset.add("Orange")
print(myset)

#(myset[1])
#myset.pop("Orange")
print(myset)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)