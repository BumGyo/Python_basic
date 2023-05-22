# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:01:13 2023

@author: 208-PC
"""

a = [1, 2, 3, 4, 5]
b = [1, 3, 3, 4, 5, 6, 7]

result = [i for i in a if i in b]
print("결과= ", result)