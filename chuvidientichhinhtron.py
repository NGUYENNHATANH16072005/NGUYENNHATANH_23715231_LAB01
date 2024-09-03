# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:22:16 2024

@author: nhat anh
"""
import math
bankinh = float(input("Nhập vào bán kính của hình tròn: "))
chuvi = 2 * math.pi * bankinh
dientich = math.pi * bankinh ** 2
print("Chu vi của hình tròn là: ", round(chuvi, 2))
print("Diện tích của hình tròn là: ", round(dientich, 2))