# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:43:12 2024

@author: nhat anh
"""
a = int(input("Nhập vào số nguyên thứ nhất: "))
b = int(input("Nhập vào số nguyên thứ hai: "))
c = int(input("Nhập vào số nguyên thứ ba: "))
d = int(input("Nhập vào số nguyên thứ tư: "))

minnumber = a

if b < minnumber:
    minnumber = b
if c < minnumber:
    minnumber = c
if d < minnumber:
    minnumber = d

print("Số nhỏ nhất so các số trên là:", minnumber)
