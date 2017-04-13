#!/usr/bin/python

def insertion_sort(items):
        """ Implementation of insertion sort """
        for i in range(1, len(items)):
                j = i
                while j > 0 and items[j] > items[j-1]:
                        items[j], items[j-1] = items[j-1], items[j]
                        print items
                        j -= 1
        return items

lst = insertion_sort([8,3,7,9,2,5,6])
print lst
