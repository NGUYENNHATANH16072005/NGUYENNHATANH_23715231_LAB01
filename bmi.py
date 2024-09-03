# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:32:39 2024

@author: nhat anh
"""
cannang = float(input("Nhập vào số cân nặng của bạn (kg): "))
chieucao = float(input("Nhập vào số chiều cao của bạn (m): "))
BMI = cannang/(chieucao**2)
print("Chỉ số BMI của bạn là: ")
if BMI < 18.5:
    print("Bạn đang gầy và thiếu cân")
elif 18.5 <= BMI <24.9:
    print("Bạn đang bình thường, ở mức lí tưởng")
elif 25 <= BMI < 29.9:
    print("Bạn đang thừa cân, cần điều chỉnh chế độ ăn")
else:
    print("Bạn bị béo phì, cần có kế hoạch giảm cân phù hợp và khoa học")
