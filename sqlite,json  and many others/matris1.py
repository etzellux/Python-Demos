list1=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    for j in range(0,3):
        print(str(list1[i][j])+" ",end="")
    print("")
    
print("***************")
list1_transpoze=[[ tm[k] for tm in list1] for k in range(3)]
print(list1_transpoze)
        
    


