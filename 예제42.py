# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:02:44 2023

@author: 208-PC
"""

list_a = [1, 2, 3, 4, 5, 6]
#f = lambda x : 2*x
# result = map(f, list_a)
result = filter(lambda x : x%2 == 0, list_a)
print(list(result))