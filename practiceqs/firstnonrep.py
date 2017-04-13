#!/bin/python

def findfirstnonrep(a):
    dicts = {}
    for c in a:
        dicts[c] = 'false'
    for c in a:
        if dicts[c] == 'false':
            return c
        else:
            dicts[c] = 'True'

print(findfirstnonrep('aparna'))
