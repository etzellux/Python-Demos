#DERS9: EKSIK VERILER
#KUTUPHANE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#VERI EKLEME
veriler = pd.read_csv("eksikveriler.csv")

#VERI ON ISLEME
print(veriler)
#EKSIK VERILER
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0) #Eksik verilerin databasedeki gösterimi, eksik verileri tamamlama stratejisi ve çalışılacak eksen belirleniyor.
Yas = veriler.iloc[:,1:4].values   #veriler listesinin 1:4e kadar ki sütunlarının tüm satırları alınıp Yas değişkenine atanıyor.
imputer = imputer.fit(Yas[:,1:4])  #fit fonksiyonu ile belirtilen arraydeki eksik değerler için uygun değer hesaplanıyor
Yas[:,1:4] = imputer.transform(Yas[:,1:4]) #Hesaplanan değer eksik yerlere dolduruluyor ve arrayin tam hali kendisine atanıyor 
print(Yas)
#ALTERNATIF VERSIYON
#VERILER DATA FRAMEINDEN ILGILI YERLERI KIRPTIKTAN SONRA
#SPLİT ETMEDEN DE BU KISIM KULLANILABILIR
# yas = veriler.iloc[:,1:4].values
# imputer = imputer.fit(yas)
# yas = imputer.transform(yas)
