# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:58:50 2024

@author: nhat anh
"""
a = float(input("Nhập vào số thứ nhất: "))
b = float(input("Nhập vào số thứ hai: "))
if a != 0:
    print("Phương trình có một nghiệm duy nhất: x = ", -b/a )
else:
    if b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có vô số nghiệm")
        