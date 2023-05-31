# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:48:24 2023

@author: 208-PC
"""

text = """101 COM PythonProgramming
102 MAT LinearAlgebra
103 ENG ComputerEnglish"""

import re
s = re.findall("\d+", text)
print(s)