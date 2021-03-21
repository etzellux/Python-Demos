# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 22:52:06 2021

@author: etzellux
"""

file = open("deneme.txt","r+")

text = file.read(2)

position = file.tell()

file.seek(0,0)

print(text)
