# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:13:32 2023

@author: 208-PC
"""

# 윈도우를 만들어주는 함수를 임포트
from tkinter import *

# win 변수에 기본 윈도우 생성
win = Tk()
# 창 이름(title) : 윈도우 창
win.title("윈도우 창")
# 창 크기(geometry) : 가로 300 x 세로 200
win.geometry('300x200')
# width(가로) 크기변경 가능, hight(세로) 크기변경 불가
win.resizable(width = True, height = False)
# 레이블 위젯 만듦
label = Label(win, text = 'Label 만들었음')
# win과 결합
label.pack()

# 기본 윈도우의 기능 활성화
win.mainloop()