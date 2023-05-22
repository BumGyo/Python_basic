# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:02:55 2023

@author: 208-PC
"""

class Counter :
    # 생성자는 class로부터 인스턴스가 생성될때 가장먼저 실행된다.
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        
# a라는 인스턴스를 생성해준다.
a = Counter()
# a 클래스의 increment() 함수를 실행시킨다.
a.increment()
print("카운터의 값=", a.count)