# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:40:43 2026

@author: adity
"""

s = input("enter sentence= ")

i = 0
capital = 0
small = 0
digit = 0
special = 0

while i < len(s):
    if 'A' <= s[i] <= 'Z':
        capital += 1
    elif 'a' <= s[i] <= 'z':
        small += 1
    elif '0' <= s[i] <= '9':
        digit += 1
    else:
        special += 1

    i += 1

print("Capital letters:", capital)
print("Small letters:", small)
print("Digits:", digit)
print("Special characters:", special)