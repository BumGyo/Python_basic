# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:06:33 2023

@author: 208-PC
"""

values = [0] * 10
print(values)
b = [x for x in range(1, 11) ]
print(b)
c = [x*2 for x in range(1, 6)]
print(c)
d = [x**2 for x in range(1, 11)]
print(d)

aList = [10,20,30,40,50,60]
del aList[0:3]
print(aList)

e = [10,20,30,40,50]
print(e[-2])
print(e[-3:-1])

print(e[::-2])

f = [x+y for x in ['Hello', 'Good'] for y in ['World', 'Bye']]
print(f)

g = ['xyz', 'zz', 'PQRTUVWZ']
print(max(g))

z = [1,2,3,4]
z[1:4] = [5,6,7]
print(z)