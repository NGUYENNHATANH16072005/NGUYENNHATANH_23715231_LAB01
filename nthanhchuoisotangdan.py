# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:16:03 2024

@author: nhat anh
"""
n = int(input("Nhập vào 1 số nguyên n: "))
chuoi = list(str(n))
chuoi.sort()
chuyen_chuoi = int("".join(chuoi))
print("Các chữ số theo thứ tự tăng dần là: ", chuyen_chuoi )