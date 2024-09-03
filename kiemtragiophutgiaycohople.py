# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:06:17 2024

@author: nhat anh
"""
gio = int(input("Nhập vào số giờ: "))
phut = int(input("Nhập vào số phút: "))
giay = int(input("Nhập vào số giây: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Giờ, phút, giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ")
