# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:20:05 2024

@author: nhat anh
"""
import math 
hinh = input("Nhập hình (v: vuông, n: nhật, t: tròn): ")
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh: "))
    chuvi = canh * 4 
    dientich = canh ** 2 
    print("Chu vi của hình vuông đó là: ", chuvi)
    print("Diện tích của hình vuông đó là: ", dientich)
elif hinh == 'n':
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
    chuvi = 2 * (a+b)
    dientich = a*b
    print("Chu vi của hình chữ nhật đó là: ", chuvi)
    print("Diện tích của hình chữ nhật đó là: ", dientich)
elif hinh == 't':
    r = float(input("Nhập bán kính: "))
    chuvi = 2 * math.pi * r
    dientich = math.pi * r**2
    print("Chu vi của hình tròn đó là: ", chuvi)
    print("Diện tích của hình tròn đó là: ", dientich)
else:
    print("Hình này không hợp lệ")
    
