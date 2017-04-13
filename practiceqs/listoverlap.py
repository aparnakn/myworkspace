#!/usr/bin/python

def checkoverlap(l,m):
    a = []
    for items in l:
        if items in m and items not in a:
            a.append(items)
    #a = [ i for i in l if i in m and i not in a ] 
    print a


l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 90, 95, 96, 98, 101]
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
checkoverlap(l,m)
    
