def add_logging(orig_func):
    def logging_func(x):
        print 'Called %s() with %r' % (orig_func.__name__, x)
        answer = orig_func(x)
        print 'The answer is', answer
        return answer
    return logging_func


###################################################################

import time

def square(x):
    'returns a value times itself'
    return x * x

square = add_logging(square)

def collatz(x):
    return 3 * x + 1 if x % 2 == 1 else x // 2   

def big_func(x):
    'Simulate a slow expensive function'
    print 'Doing hard work'
    time.sleep(1)
    return x + 1

x = 10
