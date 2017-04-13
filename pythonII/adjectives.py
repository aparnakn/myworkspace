'''
Short-cut       Dunder methods          raymond Adj     real adj
---------	--------------		-----------	---------	
len(a)          a.__len__()              lennable	sizable
a[i]		a.__getitem__(i)	bracketable	indexable
a(i, j)		a.__call__(i, j)	parenable	callable
a+b		a.__add__(b)		plusable	addable
a * b		a.__mul__(b)		starable	multipliable
pw(a, b)	a.__pow__(b)
abs(a)		a.__abs__()
format(a, b='')	a.__format__(b)
iter(a)		a.__iter__() or 
  		a.__getitem__()
a / b		a.__div__(b)
		a.__truediv__(b)
print a		a.__str__()
>> a		a.__repr__()
for x in a:	a.__iter__()

