#!/bin/bash

def findlargesum(a):
    largesum = 0 
    currentsum = 0
    start, end, temp = 0,0,0
    for i in range(len(a)):
        currentsum += a[i]
        if currentsum < 0:
            currentsum = 0
            temp = i+1
        elif currentsum > largesum:
            largesum = currentsum
            start = temp
            end = i
    return largesum, a[start:end+1] 

large, lst = findlargesum([-2, 2, 5, -11, 6])
print large, lst
            
        
