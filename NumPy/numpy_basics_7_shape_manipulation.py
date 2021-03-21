#SHAPE MANIPULATION
import numpy as np
#%%
array1 = np.array(10* np.random.random((2,3,3)),dtype=int)
print(array1,"\n",)
print(array1.ravel(),"\n") #arrayin düzleştirilmiş halini döndürür

#%%
array2 = np.array([[1,2],[3,4]])
print(array2,"\n")
print(array2.T,"\n")

#%%
array3 = np.array([[1,2,3],[4,5,6]])
print(array3.reshape(3,2),"\n") #arrayin şekillendirilmiş halini döndürür
print(array3.shape,"\n")
array3.resize(3,2) #resize((n,m)) arrayi şekillendirir
print(array3)
print(array3.shape,"\n")

