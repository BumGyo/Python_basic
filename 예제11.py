# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:46:24 2023

@author: 208-PC
"""

print("===============================")
print("메뉴 1번: 치즈버거\n메뉴 2번: 치킨 버거\n메뉴 3번: 불고기버거")
print("===============================")
menu = int(input("메뉴 번호를 입력하시오: "))

if menu == 1:
    print("치즈 버거 선택됨")
elif menu == 2:
    print("치킨 버거 선택됨")
elif menu == 3:
    print("불고기 버거 선택됨")
else:
    print("잘못 입력하셨습니다.")
    