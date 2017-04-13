''' Circuitous(tm)

Apply advanced circle analytics in optimized
algorithms for cutting edge distributed circle
management tasks to save the planet.
'''

# Project name and elevator pitch
# Purpose of inheritance is for code re-use.  One class reuses the methods from another class.
# Inheriting from object creates a new-style class.
# New-style classes have a smarter __getattribute__ __setattr__ __delattr__
# The give us a more powerful, controllable, and reprogrammable dot operator
# Generally, dunder methods don't have a docstring because
# 1) user's don't see the docstring -- they are using short-cuts instead
# 2) dunder methods already have a standard meaning which usually doesn't need more explaining
# Classes usually have uppercase letters
# The instance variable is usually called "self"
# The part of "self" that is misleading is that it may
# represent an instance of a child class.
# In general, when moving data from one namespace to another,
# we usually keep the name the same.
# Magic constants should given a name (usually all CAPS) and factored-out.
# D.R.Y. -- Do not repeat yourself
#        -- There should be a single source of truth
#        -- All essential ideas should be expressed exactly once in the code
# DRY violations are a code smell
# Code smell:  Code that works and passes tests but has other maintainability/readability issues
# Indictates a new to refactor, put out the common components

# Modules exist for two reasons 1) code organization and 2) code reuse
# Related concepts:  Loose coupling and High Cohesion
# Dogfooding:  Be your own first user.
# MVP:  Minimum viable product
# Y.A.G.N.I.,R.N. -- You ain't gonna need it, right now
# "Code is your enemy"

import math
from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor', 'micro'])

class Circle(object):
    ''' Construct a new circle from its radius

        The circle class has specialized algorithms
        providing sophisticated circle analytics
    '''

    __slots__ = ['diameter']            # Saves memory by replaced instance dicts with a fixed slots for data

    version = Version(0, 9, 1)          # Class variables are SHARED by all instances

    def __init__(self, radius):
        self.radius = radius            # Instance variables should be UNIQUE to each instance

    def area(self):
        'Perform quadrature on a planar shape of uniform revolution'
        radius = self.__perimeter() / 2.0 / math.pi     # Class local reference, because sometimes you want "self" to really be you
        return math.pi * radius ** 2.0

    def perimeter(self):
        'Compute the closed line integral for the 2-D locus of points equidistant from a given point'
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter             # Double leading underscores automatically mangle the name to _Circle__perimeter

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    @staticmethod                                       # Reprogram the dot to NOT add "self" as the first argument
    def angle_to_grade(angle):                          # Use case is adding functions to classes to solve a human factors findability problem
        'Convert an inclinometer reading in degrees to a percent grade'
        return math.tan(math.radians(angle)) * 100.0      

    @classmethod                                        # Reprograms the dot to add "cls" as the first argument
    def from_bbd(cls, bbd):                             # Use case is to create alternative constructors that a subclassable
        'Create a new circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)
                   
    @property                                           # Reprograms the dot to convert attribute access like a.x into method access like a.m()
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    ''' I wish that EVERYWHERE someone (including me) wrote c.radius
        that MAGICALLY c.get_radius() would be called without me
        having to change ANY code, and I wish that EVERYWHERE someone
        (including me) c.radius=value that MAGICALLY c.set_radius(value)
        would be without me having to change ANY code.
    '''


