# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:42:43 2023

@author: 208-PC
"""

import turtle as t

t.pencolor("#FFCCBB")
for k in range(250) :
    t.pensize((300 - k) / 10)
    t.fd(k / 40)