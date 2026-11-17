# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:28:57 2026

@author: adity
"""

n = int(input("enter n= "))
if n <= 1:
    print("not prime")
else:
    prime = True
    
for i in range(2,n):
    if n % i == 0:
        prime = False
        
if prime:
    print("prime")
else:
    print("not prime")
        