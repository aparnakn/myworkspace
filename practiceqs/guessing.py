#!/usr/bin/python

import random
import sys

def guess(n):
    a = ramdom.randint(0,9)
    if n < a:
        print "you guessed a lower number"
    if n > a:
        print "you guessed a high number"
    if n == a:
        print "you guessed the right number"

print "enter a number:"
number_chose = sys.argv[1]
guess(number_chose)
