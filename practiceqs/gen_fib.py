#!/usr/bin/python

def gen_fib(n):
    if n == 0 or n == 1:
       return n 
    return (gen_fib(n-1)+gen_fib(n-2))

numb = int(input("enter how many fib series you want to generate:\n"))
a = []
for i in range(0,numb):
    a.append(gen_fib(i))
print a

