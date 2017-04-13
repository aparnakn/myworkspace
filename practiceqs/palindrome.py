#!/usr/bin/python

def ispalindrome(a):
    for i in range(0,(len(a)/2)):
        if a[i] != a[-i-1]:
            return False
    return True

result = ispalindrome("tomatootamot")
print result
