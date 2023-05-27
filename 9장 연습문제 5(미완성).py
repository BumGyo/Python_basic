# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:45:55 2023

@author: 208-PC
"""

from tkinter import *

win = Tk()

# 증가 버튼을 누르면 실행될 함수를 정의해준다.
def increase():
    # 라벨의 값을 정수로 바꿔서 count 변수에 넣는다.
    count = int(lab["text"])
    # 라벨의 값을 count에 1을 더해서 문자로 바꿔준다.
    lab["text"] = str(count+1)

# 감소 버튼을 누르면 실행될 함수를 정의해준다.
def decrease():
    count = int(lab["text"])
    lab["text"] = str(count-1)

button_dec = Button(win, text="감소", command=decrease, width=10).grid(row=0, column=0)
# 라벨의 grid를 한줄로 할 경우 자꾸 에러가 나서 두 문장으로 바꿨다.
lab = Label(win, text="0", width=10)
lab.grid(row=0, column=1)
button_inc = Button(win, text="증가", command=increase, width=10).grid(row=0, column=2)

win.mainloop()
