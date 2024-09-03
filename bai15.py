# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:08:16 2024

@author: nhat anh
"""
a = float(input("Nhập vào số a:"))
b = float(input("Nhập vào số b:"))
bt1 = a + b
bt2 = (a**(1/3)) + (b**(1/3))  
bt3 = (a * b)**(1/3)  
bt4 = a**(1/3)  
bt5 = b**(1/3) 
ketqua= ((bt1/bt2)-bt3)/(bt4-bt5)**2 
print ("Kết quả của biểu thức trên là: ", round(ketqua,3))
