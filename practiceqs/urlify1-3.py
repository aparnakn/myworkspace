#!/bin/python

def urlify(a):
    b = '%20'.join(a.split())
    return b

print urlify("Mr John Smith")
