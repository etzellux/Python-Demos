#ARRAY INDEXES AND SLICES
import numpy as np 

array1 = np.array([[2,3],[4,5]])

print(array1[:,:],"\n")
print(array1[0:2,0:1],"\n")
print(array1[0:2,1:2],"\n")
#%%
array2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(array2.shape)
print(array2[:,:,:],"\n")
print(array2[:,:,0:2],"\n")
print(array2[:,0:1,:])


#%%
array3 = np.arange(0,20,2)

print(array3,"\n")

array3[3:10:2] = -100

print(array3,"\n")

#%%
array4 = np.arange(0,10,1)

print(array4[::-1])