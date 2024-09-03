# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:24:09 2024

@author: nhat anh
"""
a = int(input("Nhập số giờ của bạn: "))
b = int(input("Nhập số phút của bạn: "))
c = int(input("Nhập số phút của bạn: "))
if a<= 24 and b<= 60 and c<=60:
    Giay = a*3600 + b*60 + c
    print(f"{a} giờ {b} phút {c} giây tương đương với {Giay} giây")
else:
    print("Giờ, phút và giây của bạn nhập không hợp lệ ")
