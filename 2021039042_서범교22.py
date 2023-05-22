# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:58:52 2023

@author: 208-PC
"""

class BankAccount:
    def __init__(self) :
        self.__balance = 0
        
    def withdraw(self, amount) :
        self.__balance -= amount
        print("통장에 ", amount, "가 출금되었음")
        return self.__balance
    
    def deposit(self, amount) :
        self.__balance += amount
        print("통장에 ", amount, "가 입금되었음")
        return self.__balance
    
    def show_balance(self) :
        print("현재 잔액은", self.__balance, "입니다.")
    
a = BankAccount()
a.deposit(100)
a.withdraw(10)
a.show_balance()