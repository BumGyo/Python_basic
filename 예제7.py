# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:01:57 2023

@author: 208-PC
"""

import random

x = random.randint(1, 100)
y = random.randint(1, 100)


result = int(input(f"{x} + {y} ="))

if(result == x + y):
    print("True")
else:
    print("False")