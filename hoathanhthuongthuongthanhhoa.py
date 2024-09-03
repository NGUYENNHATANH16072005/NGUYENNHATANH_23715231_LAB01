# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:08:48 2024

@author: nhat anh
"""
chucai = input("Nhập vào một chữ cái: ")
if chucai.islower():
    kytu = chucai.upper()
else:
    kytu = chucai.lower()
print("Chữ cái sau khi chuyển đổi: ", kytu)
