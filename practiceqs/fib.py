#!/usr/bin/python

fib_dict = {}


def cache_fib(fib_func):
    print 'inside cache_fib'

    def fib_wrapper(n):
        if n not in fib_dict:
	    fib_dict[n] = fib_func(n)
        return fib_dict[n]

    return fib_wrapper

@cache_fib    
def fib(n):
    print 'aparna looses'
    if n == 0 or n ==1:
        return n 
    return fib(n-1)+fib(n-2)

#fib = cache_fib(fib)

result = fib(10)
print result



