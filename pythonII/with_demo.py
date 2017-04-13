# how to open and close files the old way

f = open('notes2/hamlet.txt')
try:
    play = f.read()
    print len(play)
finally:
    f.close()

# new way

with open('notes2/hamlet.txt') as f:
    play = f.read()
    print len(play)

#how to create locks

import threading

printer_lock = threading.Lock()

#use loacks old way

printer_lock.acquire()
try:
    print 'critical section 1'
    print 'critical section 2'
finally:
    printer_lock.release()

#use lock new way

with printer_lock:
    print 'critical section 1'
    print 'critical section 2'

## how to context managers work ########

class CM:
    'A fully featured context manager'
    def __init__(self, x):
        self.x = x

    def __enter__(self):
        print 'Entering and returning 42'
        return 42

    def __exit__(self, exctype, excinst, exctb):
        print 'Existing'
        print 'x is still', self.x
        print 'Exctype:', exctype
        if issubclass(exctype, KeyError):
            print 'Caught a KeyError'
            print 'the arguments are', excinst.args
            print 'Returning True to mark the exception as handled'
            return True
        print 'Returning None (which is false) meaning unhandled exception'

# Normal case ####################

print 'Starting up', '-'*20
with CM(10) as y:
    print 'In the body with y = ', y
    print 'In the middle'
    print 'At the end'
print 'Done'

# Handle exception #########

print 'Starting up', '-'*20
with CM(10) as y:
    print 'In the body with y = ', y
    print 'In the middle'
    raise KeyError('tom')
    print 'At the end'
print 'Done'

# unHandle exception #########

print 'Starting up', '-'*20
try:
    with CM(10) as y:
        print 'In the body with y = ', y
        print 'In the middle'
        raise RuntimeError('Kronecker products again')
        print 'At the end'
    print 'Done'


