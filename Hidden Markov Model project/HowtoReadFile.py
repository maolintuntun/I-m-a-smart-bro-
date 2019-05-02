# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:54:10 2019

@author: diyeq
"""


a = []

filename = "InputFile7.txt"

with open (filename,"r") as f:
    f.readline()
    f.readline()
    print(f.readline())
    for i in range(4): #directly skip all the lines before
        f.readline()  
 
# =============================================================================
#     a = [p for p in f.readline()[1: -1].split(',')]
#     print(a) 也对
# =============================================================================
    for p in f.readline()[1:-1].split(','):
        a.append(int(p))
    print(a)  #recommend! clear. put the loop out
    
f.close() # After all the readline() end .
    
    