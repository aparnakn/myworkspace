#!/bin/python

def isunique(a):
    for i in range(0,(len(a)-1)):
        if a[i] in a[i+1:]:
            return False
        else:
            return True


print isunique('abcdef')
