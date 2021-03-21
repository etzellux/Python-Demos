list1= list(((x,y,z),(x,x+y,z)) for x in range(3) for y in range(3) for z in range(3))
print(list1)
print(len(list1[0]))
#%% ARGUMENT LISTS AND DICTS
def function1 (**a):
    for i in a:
        print(str(i),"=",str(a[i]))
    
function1(abc=9,b=5)