#STACKING ARRAYS TOGETHER
import numpy as np
#%%
array1 = np.array(10*np.random.random((3,3)),dtype=int)

array2 = np.array(10*np.random.random((3,3)),dtype=int)

print(np.vstack((array1,array2)),"\n") #dikey olarak stackler

print(np.hstack((array1,array2)),"\n") #yatay olarak stackler

#%%
array3 = np.array([1,2,3])

array4 = np.array([4,5,6])

array5 = np.column_stack((array3,array4)) #1d arrayleri sütun olarak birleştirir

array6 = np.row_stack((array3,array4)) #1d arrayleri satır olarak birleştirir
#%%


