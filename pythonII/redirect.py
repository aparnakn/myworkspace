from dis import dis
import sys, os
from StringIO import StringIO

class RedirectStdout:
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.oldstdout = sys.stdout
        sys.stdout = self.target
        return self.target

    def __exit__(self, exctype, excinsr, exctb):
        sys.stdout = self.oldstdout


def show_family(lastname, first_names):
    'Display family memebers in a nice tabular form'
    print 'The %s Family' % lastname.title()
    print '=' * (11 + len(lastname))
    for name in first_names:
        print '* %s' % name.title()
    print

with RedirectStdout(target=sys.stderr):
    show_family('bharadwaj', 'aparna shashank vimala'.split())

f = open('family.dis', 'w')
try:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        dis(show_family)
    finally:
        sys.stdout = oldstdout
finally:
    f.close()

with open('help.txt', 'w') as f:
    with RedirectStdout(target = f):
        help(show_family)

with open('help.txt') as f:
    s = f.read()
    print s.upper()
try:
    os.remove('help.txt')
except OSError:
    pass


f = StringIO()
try:
    with RedirectStdout(target=f):
        help(show_family)
    print f.getvalue().upper()
finally:
    f.close()
