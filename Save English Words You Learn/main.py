# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:59:39 2021

@author: etzellux
"""

import json
import sys

def read():
    """ Read from json file"""
    
    infile = open("record.json","r")
    
    data = json.load(infile)
    
    infile.close()
    
    return data
        
    
    
def write():
    """ Write to json file"""
    
    data = read()
    
    dictionary = {}
    
    key = input("Please enter the key: ")
    value = input("Please enter the value:")
    
    dictionary[key] = value
    
    outfile = open("record.json","w")
    
    data.append(dictionary)
    
    json.dump(data,outfile)
    
    outfile.close()


while True:
    
    try:
        print("*"*30)
        print("For reading --> 1\nFor recording --> 2")  
        control = int(input("Entry:"))
        print("*"*30)
    
    except ValueError:
        print("Invalid Entry")
    
    if control == 1:
        data = read()
        
        print("")
        for i in range(0,len(data)):
            tempDict = data[i]
            
            keys = list(tempDict.keys())
            values = list(tempDict.values())
            print(keys[0] + " : " + values[0])
        print("")
        
    elif control == 2:
        write()
    elif control == 0:
        sys.exit()
    else:
        print("Invalid entry")
    
