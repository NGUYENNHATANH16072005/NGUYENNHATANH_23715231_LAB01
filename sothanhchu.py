# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:55:30 2024

@author: nhat anh
"""
so = int(input("Nhập vào một số:  "))
sobangchu = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
if 0 <= so <= 9:
    print("Số bằng chữ là: ", sobangchu[so])
else:
    print("Không đọc được")
