#'learn to group using defaultdict'

from collections import defaultdict
from pprint import pprint

names = '''
    raymond rachel matthew susan rodney david sue mark
    martin shelly davin dave bill bob dolly hank adam
    bill mary betty able henry
    '''.split()

d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)
pprint(dict(d))


d = defaultdict(set)
for name in names:
    feature = len(name) 
    d[feature].add(name)
pprint(dict(d))
