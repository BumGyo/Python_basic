# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:56:49 2023

@author: 208-PC
"""

infile = open("c:\\RSP\input.txt", "r", encoding='UTF8')
line = infile.readline()
while line !="":
    print(line)
    line = infile.readline().rstrip()