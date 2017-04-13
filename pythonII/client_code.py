"Show-off the Circuitous code from the user's point of view"

from __future__ import division
from circuitous import Circle

print u'Tutorial for Circuitous\N{trade mark sign}'
print 'Circle class version %d.%d' % Circle.version[:2]
c = Circle(10)
print 'a circle with a radius of', c.radius
print 'has an area of', c.area()
print

## Academia ########################################################

from pprint import pprint
from random import random, seed

n = 10000
jenny = 8675309
seed(jenny)
print 'DARPA Grant Proposal to study the average area of random circles'
print 'using Circuitous(tm) version %d.%d' % Circle.version[:2]
print 'preliminary study of {n} random circles'.format(n=n)
print "seeded using Jenny's number: {jenny}".format(jenny=jenny)
circles = [Circle(random()) for i in xrange(n)]
areas = [circle.area() for circle in circles]
average_area = sum(areas) / n
print 'The average area is %.5f' % average_area
print

## Rubber Sheet Company ###############################################

cut_template = [0.1, 0.2, 0.7]
print 'Specification sheet for the cut template:', cut_template
circles = [Circle(cut_radius) for cut_radius in cut_template]
for i, c in enumerate(circles, start=1):
    print 'Circle number #%d' % i
    print 'A rubber circle with a cut radius of', c.radius
    print 'has a perimeter of', c.perimeter()
    print 'and a cold area of', c.area()
    c.radius *= 1.1
    # c.set_radius(c.get_radius() * 1.1)
    print 'and a warm area of', c.area()
    print

## National Tire Company ##############################################

class Tire(Circle):
    'Circle analytics on a rubber tire'

    RUBBER_RATIO = 1.25

    def perimeter(self):
        'Circumference corrected for the rubber on the tire'
        return Circle.perimeter(self) * self.RUBBER_RATIO           # Extending
        return 2.0 * math.pi * self.radius * self.RUBBER_RATIO      # Overriding

    __perimeter = perimeter

class MonsterTire(Tire):

    RUBBER_RATIO = 1.50

t = Tire(30)
print 'A tire with an inner radius of', t.radius
print 'has an inner area of', t.area()
print 'and an outer perimeter of', t.perimeter()
print

m = MonsterTire(30)
print 'A tire with an inner radius of', m.radius
print 'has an inner area of', m.area()
print 'and an outer perimeter of', m.perimeter()
print

## National Trucking Company ###############################

print u'An inclinometer reading of 5\N{degree sign}',
print 'is a %.1f%% grade.' % Circle.angle_to_grade(5)
print

## National Graphics Company ###############################

c = Circle.from_bbd(30)
print 'A circle with a bounding box diagonal of 30'
print 'has a radius of', c.radius
print 'an area of', c.area()
print 'and perimeter of', c.perimeter()
print

## US Government ###########################################

# No circle software shall compute the area() directly from
# instance variables.  It MUST first call perimeter() and
# infer the radius indirectly.

# No circle software shall store a radius.  It MUST store
# the diameter and ONLY the diameter.
