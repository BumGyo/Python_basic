# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:26:12 2023

@author: 208-PC
"""

a = [x for x in range(1, 11)]
filtered_a = list(filter(lambda x : x % 2 == 0, a))
cub_filtered_a = list(map(lambda x : x**2, filtered_a))

print(cub_filtered_a)