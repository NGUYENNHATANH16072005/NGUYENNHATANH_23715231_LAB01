# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:58:46 2024

@author: nhat anh
"""
ngay = int(input("Nhập vào ngày sinh tương ứng: "))
thang = int(input("Nhập vào tháng sinh tương ứng: "))
nam = int(input("Nhập vào năm sinh tương ứng: "))

print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{thang}/{ngay}")
