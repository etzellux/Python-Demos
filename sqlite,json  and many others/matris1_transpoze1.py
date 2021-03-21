list1=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    for j in range(0,3):
        print(str(list1[i][j])+" ",end="")
    print("")
tm=[[0,0,0],[0,0,0],[0,0,0]]
print("***************")
for k in range(3):
    for l in range(3):
        tm[k][l]=list1[l][k]
        print(tm[k][l],end=" ")
    print("")
