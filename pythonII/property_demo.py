'''
Use the property setter when:
 * The effect of setting is obvious
 * When the underlying values can be changed
 * When the adjustment is cheap 

Dont use a property setter:
 * when the effect is ambiguous 
 * Instead use a plain method with a clear name
 * When the change is expensive, a method call makes the costs involves more clear
 
Managed attributes:
 * Control all access to an instance variable
 * This lets you range check or type validate BEFORE 

'''
from __future__ import division

class PriceRange(object):

    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    @property
    def midpoint(self):
        return (self.low + self.high) / 2.0

    def recenter_with_constant_range(self, new_midpoint):
        half = (self.high - self.low) / 2.0
        self.low = new_midpoint - half
        self.high = new_midpoint + half

    def recenter_with_constant_lo_high_ratio(self,
        pass
 
    def set_low(self, low):
        if not isinstance(low, (int, float)):
            raise TypeError('Expected int or float')
        if low < 0.0 or low > 100.0:
            raise ValueError('Expected 0 to 100')
        self._low = low 

    def get_low(self):
        return self._low

    low = property(get_low, set_low)

p = PriceRange('CSCO', 28, 33)
