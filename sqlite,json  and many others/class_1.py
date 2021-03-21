class Mathematic:
    a = None
    b = None
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def topla(self):
        print(str(self.a+self.b))
    

mat1 = Mathematic(2,11)
print(mat1.a)
print(mat1.b)
mat1.topla()
    