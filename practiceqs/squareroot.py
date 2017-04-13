#!/bin/python
#find the square root of the number to 0.1 dec

def sq_root(n):
    low = 0
    high = n
    while True:
        a = (low+high)/2.0
        #print high, low
        if a**2 == n or n-0.1 < a**2 < n+0.1: 
            return a 
        elif a**2 > n:
            high = a
        elif a**2 < n:
            low = a
