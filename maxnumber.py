# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:48:04 2024

@author: nhat anh
"""
a = int(input("Nhập vào số nguyên thứ nhất: "))
b = int(input("Nhập vào số nguyên thứ hai: "))
c = int(input("Nhập vào số nguyên thứ ba: "))

maxnumber = a
if b > maxnumber:
    maxnumber = b
if c > maxnumber:
    maxnumber = c
    
print("Số nguyên lớn nhất so với các số trên là:", maxnumber)
