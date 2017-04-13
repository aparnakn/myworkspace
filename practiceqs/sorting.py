#!/usr/bin/python


def sortfunc(lst):
    sortedlist = []
    for k in range(0,len(lst)):
        for i in range(0,(len(lst)-1-k)):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst 

listsort = sortfunc([3,4,1,2,1,3])
print listsort


