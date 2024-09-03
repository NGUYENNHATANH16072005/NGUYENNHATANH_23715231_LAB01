# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:46:10 2024

@author: nhat anh
"""
bienso = input("Nhập biển số xe của bạn ( gồm 4 chữ số): ")
tong = int(bienso[0]) + int(bienso[1]) + int(bienso[2]) + int(bienso[3])
so_nut_cua_ban_la = tong % 10
print("Số nút của biển số xe bạn là: ", so_nut_cua_ban_la)
