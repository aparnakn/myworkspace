#!/usr/bin/python

def remove_dups(a):
    b = []
    for i in range(0,len(a)):
        if a[i] not in b:
            b.append(a[i])
    return b

lst = remove_dups([2,3,4,1,2,3,6,7,4,5])
print lst
