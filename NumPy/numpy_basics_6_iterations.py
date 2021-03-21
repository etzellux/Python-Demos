#ITERATION
import numpy as np
#%%
array1 = np.arange(0,12,1).reshape((2,2,3))

#print(array1,"\n")
for i in array1:
    for j in i:
        for k in j:
            print(k," ",end="")
#%%   
for i in array1.flat:
    print(i," ",end="")