# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:42:55 2020

@author: etzellux
"""

class parent:
    
    name = "parent"
    num = 0
    def __init__(self,name,num):
        assert type(num) == int, "num integer olmali"
        self.num = num
        self.name = name
        
    def display(self):
        print("name:" + self.name + "\nnum:" + str(self.num))
        
class child(parent):
    def __init__(self,name,num):
        parent.__init__(self, name, num)
        
    def display(self):
        print(self.__dict__)
        
    
        
p1 = parent("incst1",1)
c1 = child("incst2",2)

print(isinstance(c1,child))
p1.display()
c1.display()



