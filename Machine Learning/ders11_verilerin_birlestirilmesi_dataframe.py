#DERS10: NOMINAL VERILER
#KUTUPHANELER
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#VERI YUKLEME

veriler = pd.read_csv("eksikveriler.csv")
print(veriler)

#VERI ON ISLEME
#EKSIK VERILER
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
Yas = veriler.iloc[:,1:4].values
Yas = imputer.fit_transform(Yas)
print(Yas)
cinsiyet = veriler.iloc[:,4].values
#NOMINAL VERILER -----> NUMERIC VERILER
ulke = veriler.iloc[:,0:1].values
print(ulke)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0]) #Tek sütun olduğu için 0:1 değil 0 ile sütunu belirttik(column number)
print(ulke) 
ohe = OneHotEncoder(categorical_features="all")
ulke= ohe.fit_transform(ulke).toarray()
print(ulke)
#VERILERIN BIRLESTIRILMESI
sonuc = pd.DataFrame(data = ulke,index = range(0,22,1), columns = ["fr","tr","us"])
print(sonuc)
sonuc2 = pd.DataFrame(data = Yas,index = range(0,22,1),columns = ["boy","kilo","yas"])
print(sonuc2)
sonuc3 = pd.DataFrame(data = cinsiyet,index = range(0,22,1),columns = ["cinsiyet"])
s1 = pd.concat([sonuc,sonuc2],axis = 1)
s2 = pd.concat([s1,sonuc3],axis=1)
print(s2)


