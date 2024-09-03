# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:35:35 2024

@author: nhat anh
"""
n = int(input("Nhập vào số nguyên dương n có 2 chữ số:"))
if 10 <= n <= 99 :
    chusohangchuc = n // 10
    chusohangdonvi = n % 10
    tongcacchuso = chusohangchuc + chusohangdonvi
    print("Tổng các chữ số của", n, "là:", tongcacchuso)
else:
    print("Số bạn nhập không phải là số nguyên dương có 2 chữ số")

