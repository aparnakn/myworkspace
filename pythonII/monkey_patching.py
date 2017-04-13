''' Monkey patching is making variable assignments into someone else's namespace.
    Einstein would call it, "spooky action at a distance".

    Legitimate use cases:
    * Fixing erroneous constants
    * Fixing bad, incorrect, or misleading error messages
    * Improving the robustness of a function (expanding the domain of allowable inputs)
    * Adding tempory debugging logic

    Illegitimage use cases:
    * If you ever monkey patch your own code, you are living in a state of sin
      and deserve all the maintenance problems that ensue.

'''


import algebra
import math

algebra.pi = math.pi                            # This is a monkey patch!

orig_area_tri = algebra.area_triangle           # Step 1: Save the the original

def better_area_tri(base, height):              # Step 2: Write a wrapper
    'Wrapper around algebra.area_triangle to fix a bad error message'
    try:
        return orig_area_tri(base, height)
    except RuntimeError:
        raise ValueError('Negative base or height not supported')

algebra.area_triangle = better_area_tri         # Step 3: Monkey patch

orig_sqrt = math.sqrt                           # Step 1: Save the the original

def better_sqrt(x):
    'Wrap math.sqrt to expand the domain to include negative inputs'
    if x >= 0.0:
        return orig_sqrt(x)
    return orig_sqrt(-x) * 1j

math.sqrt = better_sqrt

#########################################################################

if __name__ == '__main__':

    print u'My sources tell me the \N{greek small letter pi} =', algebra.pi
    print 'and that the area of a circle of radius ten is', algebra.area(10)

    print 'The area of the 1st triangle is', algebra.area_triangle(7, 5)
    try:
        print 'The area of the 2nd triangle is', algebra.area_triangle(-10, 20)
    except ValueError:
        print 'Oops, I did it again!'

    print u'The solutions to 12x\N{superscript two} + 23x + 10 = 0 are:'
    print algebra.quadratic(a=12, b=23, c=10)
    print u'The solutions to 12x\N{superscript two} + 8x + 10 = 0 are:'
    print algebra.quadratic(a=12, b=8, c=10)

