#DERS:7 VERILERIN YUKLENMESI
#KUTUPHANELER
import pandas as pd            #veri işlemleri için
import numpy as np             #hesaplama işlemleri için
import matplotlib as plt       #çizimler için kullanılır

#KODLAR
#--VERİ YUKLEME
veriler = pd.read_csv("veriler.csv")
print(veriler)
boykilo = veriler[["boy","kilo"]]
print(boykilo)








#--VERİ ÖN İŞLEME 
    


