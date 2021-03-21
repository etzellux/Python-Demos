#OPERATORS

import numpy as np

list1 = np.arange(0,9,1).reshape(3,3)

list2 = np.arange(9,18,1).reshape(3,3)

list3 = np.array(list1*list2)

list4 = np.array(np.cross(list1,list2)) #cross çarpım

list5 = np.array(list1.dot(list2)) #nokta çarpım

list6 = np.array(list1 @ list2)  #nokta çarpım

list7 = np.ones((3,3))

list8 = np.random.random((3,3)) #(n,m)

list9 = list7 + list8

list10 = np.random.randint(0,20,5) #(low,high,size)

print(list10.max()) #arrayin maxını verir

print(list10.min()) #arrayin minini verir

print(list10.sum()) #arraydeki sayilari toplar

print(list1.sum(axis=0)) #sütuna göre toplam

print(list1.sum(axis=1)) #satıra göre toplam

print(list1.min(axis=1)) #satırdaki en küçük sayılar

