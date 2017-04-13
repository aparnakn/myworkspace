Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> 
>>> 


>>> 
>>> # pycharm  wing-ide    spyder
>>> # eclipse (pydev)      visual studio (pydev)
>>> # vi                   emacs
>>> 
>>> # http://bit.ly/python-sj159
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> __name__          # dunder name
'__main__'
>>> # ^-- default value for __name__
>>> # ^-- an import reassigns __name__
>>> import algebra
>>> algebra.__name__
'algebra'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> __name__
'__main__'
>>> __doc__
' Docstring\n'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> area(10)
314.15700000000004
>>> 
>>> 
>>> 1.1 + 2.2 == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003
>>> 1.1 + 2.2 - 3.3
4.440892098500626e-16
>>> ['hello', 'goodbye'] * 5
['hello', 'goodbye', 'hello', 'goodbye', 'hello', 'goodbye', 'hello', 'goodbye', 'hello', 'goodbye']
>>> [0.1] * 10
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
>>> sum([0.1] * 10)
0.9999999999999999
>>> sum([0.1] * 10) == 1.0
False
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
>>> help(area)
Help on function area in module __main__:

area(radius)
    Compute the area of a circle
    
    >>> area(10)
    314.15700000000004

>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 16, in __main__.area
Failed example:
    area(10)
Expected:
    314.15700000000004
Got:
    314.157723374058
**********************************************************************
1 items had failures:
   1 of   1 in __main__.area
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 16, in __main__.area
Failed example:
    area(10)
Expected:
    314.15700000000004 
Got:
    314.15700000000004
**********************************************************************
1 items had failures:
   1 of   1 in __main__.area
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> average([10, 20, 60])
30
>>> average([10, 20, 61])
30
>>> 38 / 5
7
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=1)
>>> average([10, 20, 60])
30.0
>>> average([10, 20, 61])
30.333333333333332
>>> 
>>> from dis import dis
>>> def f(x, y):
	return x / y

>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_FAST                1 (y)
              6 BINARY_DIVIDE       
              7 RETURN_VALUE        
>>> from __future__ import division
>>> def f(x, y):
	return x / y

>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_FAST                1 (y)
              6 BINARY_TRUE_DIVIDE  
              7 RETURN_VALUE        
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> 
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 27, in __main__.average
Failed example:
    average([10, 20, 60])
Expected:
    30.0
Got:
    30
**********************************************************************
File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 29, in __main__.average
Failed example:
    average([10, 20, 61])
Expected:
    30.333333333333332
Got:
    30
**********************************************************************
1 items had failures:
   2 of   2 in __main__.average
***Test Failed*** 2 failures.
TestResults(failed=2, attempted=3)
>>> area_triangle(3, 5)
7
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=3)
>>> area_triangle(30, 40)
600.0
>>> 
>>> area_triangle(-5, 7)
-17.5
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=4)
>>> area_triangle(-5, 7)

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    area_triangle(-5, 7)
  File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 44, in area_triangle
    raise RuntimeError('Imaginary numbers not supported in Kronecker product spaces')
RuntimeError: Imaginary numbers not supported in Kronecker product spaces
>>> a = 10
>>> x = 5
>>> ax^2

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    ax^2
NameError: name 'ax' is not defined
>>> a*x^2
48
>>> # ^-- bitwise XOR
>>> a*x**2
250
>>> 
>>> [10, 20, 30, 40]
[10, 20, 30, 40]
>>> [10, (20, 30), 40]
[10, (20, 30), 40]
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=4)
>>> divmod(38, 5)
(7, 3)
>>> quotient, remainder = divmod(38, 5)
>>> 
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=4)
>>> x1, x2 = quadratic(a=8, b=-14, c=15)

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    x1, x2 = quadratic(a=8, b=-14, c=15)
  File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 59, in quadratic
    discriminant = math.sqrt(b**2.0 - 4.0*a*c)
ValueError: math domain error
>>> x1, x2 = quadratic(a=8, b=14, c=15)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    x1, x2 = quadratic(a=8, b=14, c=15)
  File "/Users/raymond/Dropbox/Public/sj159/algebra.py", line 59, in quadratic
    discriminant = math.sqrt(b**2.0 - 4.0*a*c)
ValueError: math domain error
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x1, x2 = quadratic(a=8, b=-14, c=-15)
>>> x1
2.5
>>> x2
-0.75
>>> 8*x1**2 - 14*x1 - 15
0.0
>>> 8*x2**2 - 14*x2 - 15
0.0
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=9)
>>> help(quadratic)
Help on function quadratic in module __main__:

quadratic(a, b, c)
    Return the two roots of the quadratic equation:
    
        ax^2 + bx + c = 0
    
    written in Python as:
    
        a*x**2 + b*x + c == 0
    
    For example:
    
        >>> x1, x2 = quadratic(a=8, b=-14, c=-15)
        >>> x1
        2.5
        >>> x2
        -0.75
        >>> 8*x1**2 - 14*x1 - 15
        0.0
        >>> 8*x2**2 - 14*x2 - 15
        0.0

>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=9)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=9)
>>> 
>>> 
>>> 
>>> import algebra
>>> help(algebra)
Help on module algebra:

NAME
    algebra

FILE
    /Users/raymond/Dropbox/Public/sj159/algebra.py

DESCRIPTION
    Fancy, expensive math package for wealthy people
    who have forgotten all math since the 7th grade.
    
    Copyright(c) 2017 Fly-by-night Software
    All Rights Reserved

FUNCTIONS
    area(radius)
        Compute the area of a circle
        
        >>> area(10)
        314.15700000000004
    
    area_triangle(base, height)
        Compute the area of a triangle given the base and height
        
        >>> area_triangle(30, 40)
        600.0
    
    average(seq)
        Compute the arithmetic mean
        
        >>> average([10, 20, 60])
        30.0
        >>> average([10, 20, 61])
        30.333333333333332
    
    quadratic(a, b, c)
        Return the two roots of the quadratic equation:
        
            ax^2 + bx + c = 0
        
        written in Python as:
        
            a*x**2 + b*x + c == 0
        
        For example:
        
            >>> x1, x2 = quadratic(a=8, b=-14, c=-15)
            >>> x1
            2.5
            >>> x2
            -0.75
            >>> 8*x1**2 - 14*x1 - 15
            0.0
            >>> 8*x2**2 - 14*x2 - 15
            0.0

DATA
    division = _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192...
    pi = 3.14157


>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=9)
>>> 1.1 + 2.2
3.3000000000000003
>>> from decimal import Decimal
>>> Decimal('1.1') + Decimal('2.2') == Decimal('3.3')
True
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> # types          classes
>>> #
>>> # type:  int float str unicode complex  list   dict  set
>>> #  ^--   C
>>> # string module -> str class
>>> import string
>>> dir(string)
['Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_float', '_idmap', '_idmapL', '_int', '_long', '_multimap', '_re', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'atof', 'atof_error', 'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize', 'capwords', 'center', 'count', 'digits', 'expandtabs', 'find', 'hexdigits', 'index', 'index_error', 'join', 'joinfields', 'letters', 'ljust', 'lower', 'lowercase', 'lstrip', 'maketrans', 'octdigits', 'printable', 'punctuation', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitfields', 'strip', 'swapcase', 'translate', 'upper', 'uppercase', 'whitespace', 'zfill']
>>> string.upper('hello')
'HELLO'
>>> 'hello'.upper()
'HELLO'
>>> 
>>> # type:  int float str unicode complex  list   dict  set
>>> #  ^--   C
>>> #  ^-- lowercase
>>> #  ^-- immutable
>>> #  ^-- pre-existing (compiled) can't see the source code
>>> 
>>> # class:  DefaultDict
>>> #  ^--- Python
>>> #  ^-- mutable
>>> #  ^-- they were defined at runtime (heap types)
>>> 
>>> # type/class unification
>>> 
>>> class Int(int):
	def __add__(self, other):
		print 'Adding %d and %d' % (self, other)
		return int.__add__(self, other)

	
>>> a = Int(15)
>>> b = Int(20)
>>> a * b
300
>>> a + b
Adding 15 and 20
35
>>> o = object()
>>> o
<object object at 0x1004160e0>
>>> o
<object object at 0x1004160e0>
>>> object
<type 'object'>
>>> 
>>> dir(object)
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> o.x = 10

Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    o.x = 10
AttributeError: 'object' object has no attribute 'x'
>>> 
>>> 
>>> 
>>> class O(object):
	pass

>>> o = O()
>>> o.x              # o.__getattribute__('x')

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    o.x              # o.__getattribute__('x')
AttributeError: 'O' object has no attribute 'x'
>>> 
>>> 
>>> # a[x]                a.__getitem__('x')
>>> # a[x] = 10           a.__setitem__('x', 10)
>>> # del a[x]            a.__delitem__('x')
>>> 
>>> # a.x                 a.__getattribute__('x')
>>> # a.x = 10            a.__setattr__('x', 10)
>>> # del a.x             a.__delattr__('x')
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
>>> c.__class__
<class '__main__.Circle'>
>>> c.__dict__
{'rad': 10}
>>> type(c)
<class '__main__.Circle'>
>>> vars(c)
{'rad': 10}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
{'self': <__main__.Circle object at 0x10384ddd0>, 'radius': 10}
>>> vars(c)
{'rad': 10}
>>> 
>>> 
>>> import itertools
>>> import contextlib
>>> import functools
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous(tm)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
>>> d = Circle(20)
>>> 
>>> vars(c)
{'radius': 10}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
>>> d = Circle(20)
>>> vars(c)
{'radius': 10}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
>>> d = Circle(20)
>>> vars(c)
{'version': 0.1, 'radius': 10}
>>> vars(d)
{'version': 0.1, 'radius': 20}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(10)
>>> d = Circle(20)
>>> vars(c)
{'radius': 10}
>>> vars(d)
{'radius': 20}
>>> 
>>> c.version
0.1
>>> d.version
0.1
>>> # 12:34:56
>>> # 1:34:56
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
>>> # 0.1.1
>>> 0.1.1
SyntaxError: invalid syntax
>>> 
>>> 
>>> Circle.version + 0.7 >= 0.8
False
>>> Circle.version + 0.7
0.7999999999999999
>>> 
>>> 
>>> from pprint import pprint
>>> pprint(sorted(['raymond', 'rachel', 'matthew']), width=15)
['matthew',
 'rachel',
 'raymond']
>>> 'r' == 'r' and 'a' == 'a' and 'c' < 'y'
True
>>> # ^--- lexicographic sort order
>>> pprint(sorted([
	(60, 1, 900),
	(50, 9999, 9999),
]), width=25)
[(50, 9999, 9999),
 (60, 1, 900)]
>>> pprint(sorted([
	(60, 1, 900),
	(50, 9999, 9999),
	(60, 0, 999999),
]), width=25)
[(50, 9999, 9999),
 (60, 0, 999999),
 (60, 1, 900)]
>>> todo = [
	(50, 'python'),
	(90, 'go to bed'),
	(10, 'get out of bed'),
	(30, 'feed son'),
	(60, 'take son tricycling'),
]
>>> pprint(todo, width=50)
[(50, 'python'),
 (90, 'go to bed'),
 (10, 'get out of bed'),
 (30, 'feed son'),
 (60, 'take son tricycling')]
>>> pprint(sorted(todo), width=50)
[(10, 'get out of bed'),
 (30, 'feed son'),
 (50, 'python'),
 (60, 'take son tricycling'),
 (90, 'go to bed')]
>>> min(todo)
(10, 'get out of bed')
>>> max(todo)
(90, 'go to bed')
>>> from heapq import *
>>> sorted(nsmallest(3, todo), width=25)

Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    sorted(nsmallest(3, todo), width=25)
TypeError: 'width' is an invalid keyword argument for this function
>>> pprint(nsmallest(3, todo), width=25)
[(10, 'get out of bed'),
 (30, 'feed son'),
 (50, 'python')]
>>> 
>>> pprint(nlargest(3, todo), width=25)
[(90, 'go to bed'),
 (60,
  'take son tricycling'),
 (50, 'python')]
>>> 
>>> 
>>> version = '2.7.6'
>>> target_version = '2.7.8'
>>> version >= target_version
False
>>> version = '2.7.9'
>>> version >= target_version
True
>>> version = '2.7.13'
>>> version >= target_version
False
>>> version = (2, 7, 13)
>>> target_version = (2, 7, 8)
>>> version >= target_version
True
>>> 
>>> 
>>> 
>>> r = 0, 42
>>> type(r)
<type 'tuple'>
>>> len(r)
2
>>> r[0]
0
>>> r[1]
42
>>> r[:1]
(0,)
>>> a, b = r
>>> r
(0, 42)
>>> if r[0] == 0:
	print 'Happy'

	
Happy
>>> 
>>> from collections import namedtuple
>>> # namedtuple() is a factory function that make new tuple subclasses with named fields
>>> TestResults = namedtuple('TestResults', ['failed', 'attempted'])
>>> issubclass(TestResults, tuple)
True
>>> r = TestResults(0, 42)
>>> isinstance(r, TestResults)
True
>>> isinstance(r, tuple)
True
>>> len(r)
2
>>> a, b = r
>>> r[:1]
(0,)
>>> r[0]
0
>>> r[1]
42
>>> r
TestResults(failed=0, attempted=42)
>>> if r.failed == 0:
	print 'Happy'

	
Happy
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/algebra.py ==========
TestResults(failed=0, attempted=9)
>>> 
>>> 
>>> p = 170, 0.4, 0.6
>>> type(p)
<type 'tuple'>
>>> p[0]
170
>>> a, b, c = p
>>> p[:2]
(170, 0.4)
>>> if p[1] >= 0.5:
	print 'Whew, that is bright'

	
>>> if p[2] >= 0.5:
	print 'Whew, that is light'

	
Whew, that is light
>>> Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])

Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])
NameError: name 'namedtuple' is not defined
>>> from collections import namedtuple
>>> 
>>> 
>>> from collections import namedtuple
>>> Color = namedtuple('Color', ['hue', 'saturation', 'luminosity'])
>>> p = Color(170, 0.4, 0.6)
>>> p
Color(hue=170, saturation=0.4, luminosity=0.6)
>>> p.hue
170
>>> if p.saturation >= 0.5:
	print 'Whew, that is bright'

	
>>> 
>>> 
>>> import sys
>>> sys.version
'2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) \n[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]'
>>> 
>>> tuple(sys.version_info)
(2, 7, 13, 'final', 0)
>>> sys.version_info
sys.version_info(major=2, minor=7, micro=13, releaselevel='final', serial=0)
>>> sys.version_info[3]
'final'
>>> sys.version_info.releaselevel
'final'
>>> import time
>>> tuple(time.localtime())
(2017, 3, 27, 14, 0, 6, 0, 86, 1)
>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=3, tm_mday=27, tm_hour=14, tm_min=0, tm_sec=33, tm_wday=0, tm_yday=86, tm_isdst=1)
>>> 
>>> 
>>> 
>>> time.localtime().tm_isdst
1
>>> time.localtime()[-1]
1
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj159/circuitous.py", line 39, in <module>
    class Circle(object):
  File "/Users/raymond/Dropbox/Public/sj159/circuitous.py", line 46, in Circle
    version = Versio(0, 1, 1)           # Class variables are SHARED by all instances
NameError: name 'Versio' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version Version(major=0, minor=1, micro=1)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj159/client_code.py", line 6, in <module>
    print 'Circle class version %d.%d' % Circle.version
TypeError: not all arguments converted during string formatting
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj159/client_code.py", line 9, in <module>
    print 'has an area of' + c.area()
TypeError: cannot concatenate 'str' and 'float' objects
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of314.159265359

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
>>> 
>>> 
>>> from random import random
>>> random()                                 # 0.0 <= x < 1.0
0.4988573048066006
>>> seed(8675309)

Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    seed(8675309)
NameError: name 'seed' is not defined
>>> from random import *
>>> seed(8675309)
>>> random()
0.40224696110279223
>>> 
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(2, 10)
[2, 3, 4, 5, 6, 7, 8, 9]
>>> range(2, 10, 3)
[2, 5, 8]
>>> 
>>> random() * 100.0                        # 0.0 <= x < 100.0
51.02471779215914
>>> int(3.14)
3
>>> 
>>> # Simple view of floating point numbers:        Signed integer + Signed fractional
>>> #                                                   int()             frac()
>>> 
>>> x = 3.14;  int(x)
3
>>> x = -3.14; int(x)
-3
>>> x = 3.14;  int(x);  x - int(x)
3
0.14000000000000012
>>> x = -3.14;  int(x);  x - int(x)
-3
-0.14000000000000012
>>> # int() is a odd-function           int(-x) == -int(x)           Symmetric around the origin
>>> #   \--> returns an int
>>> 
>>> from math import *
>>> floor(3.14)
3.0
>>> floor(-3.14)
-4.0
>>> ceil(3.14)
4.0
>>> ceil(-3.14)
-3.0
>>> ceil(-3)
-3.0
>>> floor(-3)
-3.0
>>> # ceil/floor are assymetric around the origin
>>> # if intergral(x), then ceil(x) == floor(x); otherwise, ceil(x) == floor(x) + 1.0
>>> #   \--> returns an float
>>> 
>>> x = 3.14;  floor(x)
3.0
>>> x = 3.14;  floor(x) + 1.0
4.0
>>> x = 3.14;  -floor(-x)
4.0
>>> # ceil/floor are assymetric around the origin
>>> # if intergral(x), then ceil(x) == floor(x); otherwise, ceil(x) == floor(x) + 1.0
>>> # ceil(x) == -floor(-x)
>>> #   \--> returns an float
>>> 
>>> [int(x + 0.3) for x in range(-10, 11)]
[-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> #                                ^  ^   weird gap in int()    sometimes you get uneven stairsteps
>>> [int(x + 0.6) for x in range(-10, 11)]
[-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> [floor(x + 0.3) for x in range(-10, 11)]
[-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
>>> 
>>> 
>>> round(3.94)
4.0
>>> round(3.1)
3.0
>>> round(-3.94)
-4.0
>>> round(-3.14)
-3.0
>>> 
>>> # int() returns an int
>>> # round() ceil() floor() return a float
>>> # int / round have uneven stairsteps but at least they are symmetric around the origin
>>> # floor / ceil have even stairstep but are assymetric
>>> 
>>> # round(x) == int(x + 0.5)
>>> 
>>> round(3.14)
3.0
>>> int(3.14 + 0.5)
3
>>> round(3.94)
4.0
>>> int(3.94 + 0.5)
4
>>> 
>>> round(3.5)
4.0
>>> round(4.5)
5.0
>>> round(-3.5)
-4.0
>>> round(-4.5)
-5.0
>>> # Rounding rule:  ROUND-HALF-AWAY-FROM-ZERO
>>> 
>>> 
>>> # Changes in Python 3:
>>> # int/floor/ceil/round all produce ints
>>> # Rounding rule:  ROUND-HALF-END  (banker's rounding)
>>> 
>>> 
>>> from random import *
>>> int(random() * 100.0)                        # 0 <= x < 100
66
>>> # 7 +/- 2
>>> #    ^-- chunking
>>> 
>>> # Good API design bridges off of what people already know
>>> range(2, 10)
[2, 3, 4, 5, 6, 7, 8, 9]
>>> randrange(2, 10)
8
>>> range(1000, 2000, 100)
[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
>>> randrange(1000, 2000, 100)
1200
>>> 
>>> 
>>> outcomes = ['win', 'lose', 'draw', 'try again']
>>> n = len(outcomes)
>>> n
4
>>> outcomes[int(random() * n)]
'draw'
>>> choice(outcomes)
'draw'
>>> results = [choice(outcomes) for i in range(20)]
>>> results
['win', 'draw', 'win', 'win', 'try again', 'draw', 'lose', 'win', 'win', 'draw', 'try again', 'lose', 'try again', 'lose', 'try again', 'win', 'draw', 'try again', 'draw', 'lose']
>>> results = [outcomes[int(random() * n)] for i in range(20)]
>>> results
['try again', 'try again', 'lose', 'draw', 'lose', 'draw', 'win', 'win', 'draw', 'lose', 'try again', 'win', 'win', 'try again', 'lose', 'lose', 'win', 'draw', 'lose', 'draw']
>>> 
>>> 
>>> results = [choice(outcomes) for i in range(20)]
>>> results
['lose', 'draw', 'try again', 'draw', 'try again', 'win', 'win', 'try again', 'lose', 'try again', 'win', 'win', 'try again', 'try again', 'win', 'try again', 'lose', 'win', 'lose', 'win']
>>> results.index('lose')
0
>>> results.index('win')
5
>>> results.count('win')
7
>>> results.count('lose')
4
>>> s = 'abracadabra'
>>> len(s)
11
>>> s[0]
'a'
>>> s.index('b')
1
>>> s.index('c')
4
>>> s.count('a')
5
>>> s.count('b')
2
>>> s.count('z')
0
>>> from collections import Counter
>>> Counter('abracadabra')
Counter({'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1})
>>> Counter(results)
Counter({'win': 7, 'try again': 7, 'lose': 4, 'draw': 2})
>>> 
>>> 
>>> # A sequence is anything that is sizeable with len(s)
>>> # and indexable with s[0], s[1], s[2], ... s[len(s) - 1], IndexError
>>> 
>>> # strings, unicode, tuples, lists, array, bytearray are all sequences
>>> # All sequences have count() and index()
>>> 
>>> # To do many counts at once:  collections.Counter(seq)
>>> 
>>> s = 'abracadabra'
>>> s.index('a')
0
>>> s.index('a', 1)
3
>>> s.index('a', 4)
5
>>> s.index('a', 6)
7
>>> s.index('a', 8)
10
>>> s.index('a', 11)

Traceback (most recent call last):
  File "<pyshell#425>", line 1, in <module>
    s.index('a', 11)
ValueError: substring not found
>>> 
>>> 
>>> 
>>> def indices(seq, value):
	results = []
	i = -1
	while True:
		try:	
			i = seq.index(value, i+1)
			results.append(i)
		except ValueError:
			break
	return results

>>> indices('abracadabra', 'a')
[0, 3, 5, 7, 10]
>>> indices('abracadabra', 'b')
[1, 8]
>>> indices('abracadabra', 'c')
[4]
>>> indices('abracadabra', 'd')
[6]
>>> indices('abracadabra', 'e')
[]
>>> indices(results, 'win')
[5, 6, 10, 11, 14, 17, 19]
>>> indices(results, 'lose')
[0, 8, 16, 18]
>>> indices(results, 'draw')
[1, 3]
>>> 
>>> 
>>> Counter(results)
Counter({'win': 7, 'try again': 7, 'lose': 4, 'draw': 2})
>>> 
>>> sample(outcome, 3)

Traceback (most recent call last):
  File "<pyshell#452>", line 1, in <module>
    sample(outcome, 3)
NameError: name 'outcome' is not defined
>>> sample(outcomes, 3)
['draw', 'win', 'lose']
>>> sample(outcomes, 5)

Traceback (most recent call last):
  File "<pyshell#454>", line 1, in <module>
    sample(outcomes, 5)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 323, in sample
    raise ValueError("sample larger than population")
ValueError: sample larger than population
>>> # ^-- Sampling without replacement
>>> 
>>> 
>>> # sample(pop, 1)[0]                      sample(pop, k)                    sample(pop, len(pop))
>>> # choice                                                                   shuffle
>>> 
>>> outcomes
['win', 'lose', 'draw', 'try again']
>>> shuffle(outcomes)
>>> outcomes
['lose', 'try again', 'draw', 'win']
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
0
1
2
3
4
5
6
7
8
9
>>> range(n)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> xrange(n)
xrange(10)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
0
1
2
3
4
5
6
7
8
9
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[<circuitous.Circle object at 0x103060690>, <circuitous.Circle object at 0x103060710>, <circuitous.Circle object at 0x103060090>, <circuitous.Circle object at 0x103060750>, <circuitous.Circle object at 0x1030607d0>, <circuitous.Circle object at 0x103060810>, <circuitous.Circle object at 0x103060850>, <circuitous.Circle object at 0x1030608d0>, <circuitous.Circle object at 0x103060890>, <circuitous.Circle object at 0x103060950>]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[<circuitous.Circle object at 0x102f5cad0>,
 <circuitous.Circle object at 0x102f5cb10>,
 <circuitous.Circle object at 0x102f5cb50>,
 <circuitous.Circle object at 0x102f5cbd0>,
 <circuitous.Circle object at 0x102f5cc50>,
 <circuitous.Circle object at 0x102f5cc10>,
 <circuitous.Circle object at 0x102f5cc90>,
 <circuitous.Circle object at 0x102f5cd10>,
 <circuitous.Circle object at 0x102f5cd50>,
 <circuitous.Circle object at 0x102f5cd90>]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[0.5083179151495382,
 0.8179205041298087,
 1.384044097288627,
 2.327396215536275,
 0.24796213997951547,
 1.2924085543325607,
 1.3159672444054562,
 0.16210527294445717,
 1.591256324893598,
 0.02610381037583005]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[<bound method Circle.area of <circuitous.Circle object at 0x102f5dad0>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5db10>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5db50>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dbd0>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dc50>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dc10>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dc90>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dd10>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dd50>>,
 <bound method Circle.area of <circuitous.Circle object at 0x102f5dd90>>]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[0.5083179151495382,
 0.8179205041298087,
 1.384044097288627,
 2.327396215536275,
 0.24796213997951547,
 1.2924085543325607,
 1.3159672444054562,
 0.16210527294445717,
 1.591256324893598,
 0.02610381037583005]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.1
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.1
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[<circuitous.Circle object at 0x102f5dad0>,
 <circuitous.Circle object at 0x102f5db10>,
 <circuitous.Circle object at 0x102f5db50>,
 <circuitous.Circle object at 0x102f5dbd0>,
 <circuitous.Circle object at 0x102f5dc50>,
 <circuitous.Circle object at 0x102f5dc10>,
 <circuitous.Circle object at 0x102f5dc90>,
 <circuitous.Circle object at 0x102f5dd10>,
 <circuitous.Circle object at 0x102f5dd50>,
 <circuitous.Circle object at 0x102f5dd90>]
[0.5083179151495382,
 0.8179205041298087,
 1.384044097288627,
 2.327396215536275,
 0.24796213997951547,
 1.2924085543325607,
 1.3159672444054562,
 0.16210527294445717,
 1.591256324893598,
 0.02610381037583005]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> Circle(10)
Circle(10.000000)
>>> c = Circle(10)
>>> d = Circle(10.000000)
>>> type(c.radius)
<type 'int'>
>>> type(d.radius)
<type 'float'>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> Circle(10)
Circle(10)
>>> Circle(10.0)
Circle(10.0)
>>> c = Circle(math.pi)
>>> c
Circle(3.14159265359)
>>> d = Circle(3.14159265359)
>>> c.radius == d.radius
False
>>> c.radius, d.radius
(3.141592653589793, 3.14159265359)
>>> 
>>> print math.pi             # "stir" -> str -> string
3.14159265359
>>> math.pi                   # "repper" -> repr -> representation
3.141592653589793
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(math.pi)
>>> c
Circle(3.141592653589793)
>>> d = Circle(3.141592653589793)
>>> c.radius == d.radius
True
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[Circle(0.40224696110279223),
 Circle(0.5102471779215914),
 Circle(0.6637431122665531),
 Circle(0.8607166923395507),
 Circle(0.28094269977126785),
 Circle(0.6413941220751519),
 Circle(0.6472135534646176),
 Circle(0.22715569766295207),
 Circle(0.711696999899619),
 Circle(0.09115426983797148)]
[0.5083179151495382,
 0.8179205041298087,
 1.384044097288627,
 2.327396215536275,
 0.24796213997951547,
 1.2924085543325607,
 1.3159672444054562,
 0.16210527294445717,
 1.591256324893598,
 0.02610381037583005]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c = Circle(math.pi)
>>> c
Circle(3.141592653589793)
>>> hex(id(c))
'0x102f5c150'
>>> d = Circle(3.141592653589793)
>>> hex(id(d))
'0x102f5c150'
>>> cache
{3.141592653589793: Circle(3.141592653589793)}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: jenny
[Circle(0.40224696110279223),
 Circle(0.5102471779215914),
 Circle(0.6637431122665531),
 Circle(0.8607166923395507),
 Circle(0.28094269977126785),
 Circle(0.6413941220751519),
 Circle(0.6472135534646176),
 Circle(0.22715569766295207),
 Circle(0.711696999899619),
 Circle(0.09115426983797148)]
[0.5083179151495382,
 0.8179205041298087,
 1.384044097288627,
 2.327396215536275,
 0.24796213997951547,
 1.2924085543325607,
 1.3159672444054562,
 0.16210527294445717,
 1.591256324893598,
 0.02610381037583005]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: jenny
The average area is 0.9673482079035665
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: jenny
The average area is 1.0

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: jenny
The average area is 1.0

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
[Circle(0.1), Circle(0.2), Circle(0.7)]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
[Circle(0.1), Circle(0.2), Circle(0.7)]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
Circle(0.1)
Circle number #1
Circle(0.2)
Circle number #1
Circle(0.7)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
Circle(0.1)
Circle number #2
Circle(0.2)
Circle number #3
Circle(0.7)
>>> 
>>> 
>>> list(enumerate('abc'))
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> list(enumerate('abc', start=1))
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #0
Circle(0.1)
Circle number #1
Circle(0.2)
Circle number #2
Circle(0.7)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
Circle(0.1)
Circle number #2
Circle(0.2)
Circle number #3
Circle(0.7)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.2
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.2
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

>>> circles
[Circle(0.11000000000000001), Circle(0.22000000000000003), Circle(0.77)]
>>> c.color = 'red'
>>> vars(c)
{'color': 'red', 'radius': 0.77}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj159/client_code.py", line 58, in <module>
    print 'and an outer perimeter of', t.perimeter()
  File "/Users/raymond/Dropbox/Public/sj159/client_code.py", line 53, in perimeter
    return 2.0 * math.pi * self.radius * 1.25
NameError: global name 'math' is not defined
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

>>> m.version
Version(major=0, minor=3, micro=1)
>>> 
>>> 
>>> 
>>> c
Circle(0.77)
>>> t
Circle(30)
>>> m
Circle(30)
>>> c.__class__
<class 'circuitous.Circle'>
>>> t.__class__
<class '__main__.Tire'>
>>> m.__class__
<class '__main__.MonsterTire'>
>>> c.__class__.__name__
'Circle'
>>> t.__class__.__name__
'Tire'
>>> m.__class__.__name__
'MonsterTire'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.3
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.3
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

>>> c
Circle(0.77)
>>> t
Tire(30)
>>> m
MonsterTire(30)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> c.__name__

Traceback (most recent call last):
  File "<pyshell#516>", line 1, in <module>
    c.__name__
NameError: name 'c' is not defined
>>> c.__class__.__name__

Traceback (most recent call last):
  File "<pyshell#517>", line 1, in <module>
    c.__class__.__name__
NameError: name 'c' is not defined
>>> c = Circle(10)
>>> c.__name__

Traceback (most recent call last):
  File "<pyshell#519>", line 1, in <module>
    c.__name__
AttributeError: 'Circle' object has no attribute '__name__'
>>> Tire.__name__

Traceback (most recent call last):
  File "<pyshell#520>", line 1, in <module>
    Tire.__name__
NameError: name 'Tire' is not defined
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.4
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.4
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

>>> Tire.__name__
'Tire'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> angle_to_grade(5)
8.7488663525924
>>> 
>>> # Truckers can't find the tool
>>> dir(Circle)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'perimeter', 'version']
>>> help(Circle)
Help on class Circle in module __main__:

class Circle(__builtin__.object)
 |  Construct a new circle from its radius
 |  
 |  The circle class has specialized algorithms
 |  providing sophisticated circle analytics
 |  
 |  Methods defined here:
 |  
 |  __init__(self, radius)
 |  
 |  __repr__(self)
 |  
 |  area(self)
 |      Perform quadrature on a planar shape of uniform revolution
 |  
 |  perimeter(self)
 |      Compute the closed line integral for the 2-D locus of points equidistant from a given point
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  version = Version(major=0, minor=5, micro=1)

>>> 
>>> 
>>> # Ship captains are arriving late to their 2nd port.
>>> 
>>> 
>>> # Type I and Type II Errors
>>> # Truckers had False negatives
>>> # Ship Captains have false positives
>>> 
>>> # Brittany  Spears
>>> #  \-> Britney
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> dir(Circle)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'angle_to_grade', 'area', 'perimeter', 'version']
>>> 
>>> 
>>> Circle.angle_to_grade(Circle(1), 5)
8.7488663525924
>>> Circle.angle_to_grade(None, 5)

Traceback (most recent call last):
  File "<pyshell#542>", line 1, in <module>
    Circle.angle_to_grade(None, 5)
TypeError: unbound method angle_to_grade() must be called with Circle instance as first argument (got NoneType instance instead)
>>> c = Circle(10)
>>> c.area()
314.1592653589793
>>> # ^-- The dot does it
>>> c.__class__.__dict__['area'](c)
314.1592653589793
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> Circle.angle_to_grade(5)
8.7488663525924
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5 degrees is a 8.7488663525924 percent grade
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5 degrees
is a 8.7488663525924 percent grade

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5 degrees is a 8.7488663525924 percent grade

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5 degrees is a 8.7 percent grade

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5° is a 8.7 percent grade

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5°

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj159/client_code.py", line 77, in <module>
    print 'is a %.1f% grade' % Circle.angle_to_grade(5)
TypeError: not enough arguments for format string
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5° is a 8.7% grade

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.5
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.5
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5° is a 8.7% grade.

>>> # from
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> Circle.from_bbd(Circle(1), 30)
Circle(10.606601717798211)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> Circle.from_bbd(30)
Circle(10.606601717798211)
>>> 2 * math.sqrt(2)
2.8284271247461903
>>> math.sqrt(8)
2.8284271247461903
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.7
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.7
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5° is a 8.7% grade.

A circle with a bounding box diagonal of 30
has a radius of 10.6066017178
an area of 353.429173529
and perimeter of 66.6432440724

>>> Tire.from_bbd(25)
Circle(8.838834764831843)
>>> MonsterTire.from_bbd(25)
Circle(8.838834764831843)
>>> 
>>> 
>>> cls = Tire
>>> 
>>> cls is Tire
True
>>> cls(10)
Tire(10)
>>> cls = Circle
>>> cls(10)
Circle(10)
>>> cls = MonsterTire
>>> cls(10)
MonsterTire(10)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.7
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.7
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5° is a 8.7% grade.


Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj159/client_code.py", line 84, in <module>
    c = Circle.from_bbd(30)
TypeError: from_bbd() takes exactly 2 arguments (1 given)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> Circle.from_bbd(Circle, 30)
Circle(10.606601717798211)
>>> Tire.from_bbd(Tire, 30)
Tire(10.606601717798211)
>>> MonsterTire.from_bbd(MonsterTire, 30)
MonsterTire(10.606601717798211)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj159/client_code.py ========
Tutorial for Circuitous™
Circle class version 0.7
a circle with a radius of 10
has an area of 314.159265359

DARPA Grant Proposal to study the average area of random circles
using Circuitous(tm) version 0.7
preliminary study of 10 random circles
seeded using Jenny's number: 8675309
The average area is 1.0

Specification sheet for the cut template: [0.1, 0.2, 0.7]
Circle number #1
A rubber circle with a cut radius of 0.1
has a perimeter of 0.628318530718
and a cold area of 0.0314159265359
and a warm area of 0.0380132711084

Circle number #2
A rubber circle with a cut radius of 0.2
has a perimeter of 1.25663706144
and a cold area of 0.125663706144
and a warm area of 0.152053084434

Circle number #3
A rubber circle with a cut radius of 0.7
has a perimeter of 4.39822971503
and a cold area of 1.53938040026
and a warm area of 1.86265028431

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 235.619449019

A tire with an inner radius of 30
has an inner area of 2827.43338823
and an outer perimeter of 282.743338823

An inclinometer reading of 5° is a 8.7% grade.

A circle with a bounding box diagonal of 30
has a radius of 10.6066017178
an area of 353.429173529
and perimeter of 66.6432440724

>>> Circle.from_bbd(10)
Circle(3.5355339059327373)
>>> Tire.from_bbd(10)
Tire(3.5355339059327373)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj159/circuitous.py =========
>>> dict(raymond='red', rachel='blue')
{'rachel': 'blue', 'raymond': 'red'}
>>> dict([('raymond', 'red'), ('rachel', 'blue')])
{'rachel': 'blue', 'raymond': 'red'}
>>> dict.fromkeys(['raymond', 'rachel', 'matthew'], None)
{'matthew': None, 'rachel': None, 'raymond': None}
>>> 
>>> 
>>> class MyDict(dict):
	pass

>>> MyDict.fromkeys(['raymond', 'rachel', 'matthew'], None)
{'matthew': None, 'rachel': None, 'raymond': None}
>>> type(_)
<class '__main__.MyDict'>
>>> 
>>> from datetime import *
>>> date(2012, 2, 14)
datetime.date(2012, 2, 14)
>>> date(2012, 2, 14).weekday()
1
>>> 
>>> date.today()
datetime.date(2017, 3, 27)
>>> date.fromordinal(725000)
datetime.date(1985, 12, 25)
>>> date.fromordinal(735000)
datetime.date(2013, 5, 12)
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj159/download.py ==========
============================ Source: http://sdwa.appliomics.com/u/3967849/sj159/links.txt ===========================
                                    Starting download at Mon Mar 27 17:35:22 2017                                    
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/sj159/download.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/IntermediatePython.pdf
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/itty.py
200* OK               https://dl.dropbox.com/u/3967849/sj159/circuitous.log   --> notes2/circuitous.log     (updated) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/bottle.py
200* OK               https://dl.dropbox.com/u/3967849/sj159/links.txt        --> notes2/links.txt          (updated) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/__init__.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/PythonAwesome.pdf
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/mpl_demo.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/lru_cache.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/pexpect.py
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/spelling.py
200  OK               https://dl.dropbox.com/u/3967849/sj159/algebra.py       --> notes2/algebra.py         (updated) 
200  OK               https://dl.dropbox.com/u/3967849/sj159/day1.py          --> notes2/day1.py            (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/quadratic.tpl   --> notes2/quadratic.tpl      (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/common_passwords.txt --> notes2/common_passwords.txt (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/hamlet.txt      --> notes2/hamlet.txt         (current) 
200* OK               https://dl.dropbox.com/u/3967849/shared/graphviz.tpl    --> notes2/graphviz.tpl       (current) 
200  OK               https://dl.dropbox.com/u/3967849/sj159/circuitous.py    --> notes2/circuitous.py      (updated) 
200  OK               https://dl.dropbox.com/u/3967849/sj159/client_code.py   --> notes2/client_code.py     (updated) 
200* OK               https://dl.dropbox.com/u/3967849/shared/big.txt         --> notes2/big.txt            (current) 
304  NOT MODIFIED     https://dl.dropbox.com/u/3967849/shared/PythonTips.pdf
>>> 

>>> 
