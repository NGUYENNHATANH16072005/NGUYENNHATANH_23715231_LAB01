# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:37:18 2024

@author: nhat anh
"""

gio1 = int(input("Nhập vào số giờ thứ nhất: "))
phut1 = int(input("Nhập vào số phút thứ nhất: "))
giay1 = int(input("Nhập vào số giây thứ nhất: "))

gio2 = int(input("Nhập tiếp vào số giờ thứ hai: "))
phut2 = int(input("Nhập tiếp vào số phút thứ hai: "))
giay2 = int(input("Nhập tiếp vào số giây thứ hai: "))

thoigian1 = gio1*3600 + phut1*60 + giay1 
thoigian2 = gio2*3600 + phut2*60 + giay2

tong = thoigian1 + thoigian2
hieu = thoigian1 - thoigian2

giotong = tong // 3600 
phuttong = (tong // 3600 ) // 60 
giaytong = (tong // 3600 ) % 60 

giohieu = hieu // 3600 
phuthieu = (hieu // 3600 ) // 60 
giayhieu = (hieu // 3600 ) % 60 

print(f"Tổng hai khoảng thời gian là: {giotong} giờ, {phuttong} phút, {giaytong} giây")
print(f"Hiệu hai khoảng thời gian là: {giohieu} giờ, {phuthieu} phút, {giayhieu} giây")

