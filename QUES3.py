# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:50:35 2026

@author: Lenovo
"""

N=int(input("enter N ="))
div = 0
notdiv = 0
x = int(input("enter x= "))
while x != -999:
    if x % N == 0:
        div = div + 1
    else:
        notdiv = notdiv + 1
    x = int(input("enter x= "))
print (div)
print (notdiv)
        