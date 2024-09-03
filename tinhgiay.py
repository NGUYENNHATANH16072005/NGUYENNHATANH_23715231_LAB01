# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:44:24 2024

@author: nhat anh
"""
time = input("Nhập vào giờ, phút và giây (Theo định dạng hh:mm:ss): ")
hh,mm,ss = map(int, time.split(":"))
if 0 <= hh < 24 and 0 <= mm <60 and 0 <= ss < 60:
    Giây = hh*3600 + mm*60 + ss
    print ("Số giây là: ", Giây)
else:
    print("Giờ, phút và giây của bạn nhập chưa hợp lệ ")