#!/usr/bin/python

import re

def iprange(start_ip, count):
    ip2hex = lambda ip: ''.join('{:02x}'.format(int(x)) for x in ip.split('.'))
    hex2ip = lambda n: '.'.join([  str(int(p, 16)) for p in re.match('(..)(..)(..)(..)', n).groups() ])
    return ( hex2ip('{0:02x}'.format(int(ip2hex(start_ip), 16) + c)) for c in xrange(count) )
 
if __name__ == '__main__':
    for ip in iprange('192.168.10.10', 300):
        print ip
