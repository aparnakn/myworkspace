#!/usr/bin/python

def add_lists(a,b):
    c = []
    k = max(len(a), len(b))
    for i in range(0,k+1):
        try:
            c.append(a[i])
        except:
            pass
        try:
            c.append(b[i])
        except:
            pass
    return c

lst = add_lists([1,2,3,4], ['a','b','c', 'd', 'e', 'f'])
print lst
