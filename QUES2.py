# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:42:10 2026

@author: Lenovo
"""

x=int(input("Enter Number:"))
sum=0
while x>0:
    sum=sum + x % 10
    x=x//10
print(sum)
    
    
