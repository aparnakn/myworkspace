#!/bin/python

def perfectsquare(a):
    low = 0
    high = a
    while True:
        mid = (low+high)/2
        if mid**2 == a:
            return mid 
        elif mid**2 > a:
            high = mid
        elif mid**2 < a:
            low = mid
        elif low == high: 
            return False

print(perfectsquare(5))
        
