#%% SET 
set1= set([1,2,3,4,5])  #CONSTRACTURE GETS ONLY ONE ARGUMENT
set2= set((4,5,6,7,8))
print(set1)
print(set2)
#%% SET UNION / PIPE / OR
print(set1|set2)
print(set1.union(set2))
#%% SET INTERSECTION / AND
print(set1&set2)
print(set1.intersection(set2))
#%% SET DIFFERENCE / -
print(set1-set2) #print(set1.difference(set2))
print(set2-set1) #print(set2.difference(set1))
#%% SET SYMMETRIC DIFFERENCE / XOR
print(set1.symmetric_difference(set2))
print(set1^set2)