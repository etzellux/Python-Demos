# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:05:58 2020

@author: etzellux
"""

num1 = int(input("birinci sayi:"))

num2 = int(input("ikinci sayi:"))

sonuc = 0
try:
    sonuc = num1/num2

except:
    print("0 a bolme hatasi")
finally:
    print(sonuc)
    