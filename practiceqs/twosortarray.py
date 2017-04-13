#!/bin/python

def sort2arrays(a,b):
    l = []
    pta, ptb, ptl = 0,0,0
    while pta < len(a) and ptb < len(b):
        if a[pta] < b[ptb]:
            l.append(a[i])
            pta+=1

print sort2arrays([2,4,6,8,10], [1,3,5,7,9])
