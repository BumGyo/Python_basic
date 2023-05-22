# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:52:51 2023

@author: 208-PC
"""

from tkinter import *

# 버튼이 눌리면 실행될 함수 생성
def FtoC():
    # e1의 값을 읽어 실수형으로 형변환하여 t1 변수에 대입
    tf = float(e1.get())
    # 화씨 -> 섭씨 형변환
    tc = (tf-32.0)*5.0/9.0
    # 처음부터 끝까지 값을 초기화해줌
    e2.delete(0, END)
    # tc의 값을 문자열로 추가해줌
    e2.insert(0, str(tc))
    
window = Tk()

Label(window, text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# 버튼이 눌렸을때 발생할 이벤트를 command=함수명으로 함
Button(window, text="화씨 -> 섭씨", command=FtoC).grid(row=2, column=1)
window.mainloop()