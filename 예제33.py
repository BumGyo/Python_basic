# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:33:01 2023

@author: 208-PC
"""

# 윈도우를 만들어주는 함수를 임포트
from tkinter import *

# win 변수에 기본 윈도우 생성
window = Tk()

# 여러 특징이 있는 버튼 생성
button = Button(window, text ="클릭하세요!", bg="yellow", fg="blue", width = 80, height = 2)

# win과 결합
button.pack()

# 기본 윈도우의 기능 활성화
window.mainloop()