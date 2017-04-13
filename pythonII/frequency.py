# To make this executable, run: chmod +x frequency.py
# make it findable from anywhere:
# alias frquency = "path to the module"
#or create simlink
# ln -s 

from collections import Counter
import re

def top_words(text, limit=50, word_pattern=r"[a-z\'\-]+", case_insensitive=True):
    '''Return a list of tuples in the form [(word, count),.....]
       Result is arranged from most common to least common.
       Limit defaults to 50 but may be set to NOne to list all
       Defaults to case insensitive.
       Word pattern allows alpha and apostrophes but may be 
    '''
    if case_insensitive:
        text = text.lower()
    words = re.findall(word_pattern, text)
    return Counter(words).most_common(limit)

if __name__=='__main__':
    from pprint import pprint
    import sys

    filename = 'notes2/hamlet.txt'
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    if len(sys.argv) == 3:
        limit = int(sys.argv[2])
    if len(sys.argv) > 3 or len(sys.argv) == 2 and sys.argv[1] == '-h':
        print >> sys.stderr, 'Usage: frequency [filename [limit=10]]'
        sys.exit(1) 

    with open('notes2/hamlet.txt') as f:
        play = f.read()
    pprint(top_words(play,limit=limit))

