# ARRAY CREATION
import numpy as np

list1 = np.array([[2,3],[4,5]])

list2 = np.arange(10,20,2) #(başla,bitir,artış miktarı)

list3 = np.array([[1,2],[3,5]],dtype=complex)

list4 = np.arange(0,1,0.1)

list5 = np.zeros( (2,3) ) #( (n,m) )

list6 = np.ones( (2,5) ) #( (n,m) )

list7 = np.linspace(0,2,9) #(başla,bitir,eleman sayısı)

list8 = np.empty( (2,3) ) #( (n,m) )
