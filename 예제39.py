# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:01:19 2023

@author: 208-PC
"""

# 입력받고 출력할 파일 위치 지정해주고 권한 주기
infile = open("C:\sales.txt", "r")
outfile = open("C:\summary.txt", "w")

# 변수 선언(sum은 내장변수로 존재하지만 그냥 변수로 써도 됨)
sum = 0
count = 0

# 파일을 한줄씩 읽기 때문에 while문으로 빈칸이 나올때까지 한 줄씩 읽어준다.
line = infile.readline()
while line != "":
     s = int(line)
     sum += s
     count += 1
     line = infile.readline()

# 출력 파일에 값을 입력해준다.
outfile.write("총매출 = " + str(sum) + "\n")
outfile.write("평균 일매출 = " + str(sum/count))

# 입력을 마쳤기 때문에 파일을 닫아준다.
infile.close()
outfile.close()