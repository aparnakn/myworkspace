#!/usr/bin/python

def get_divisors(n):
    a = [ i for i in range(1,n+1) if n%i == 0]
    return a


numb = int(input("enter a number:\n"))
a = get_divisors(numb)
print a

