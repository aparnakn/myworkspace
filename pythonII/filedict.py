'''
Make a dictionary object from scratch
The ground will be file objects
The filename will be the dictionary key
The file contents witll be the dictionary value
1st: __getitem__, __setitem__, __delitem__, __iter__, __len__
2nd: get(), clear() setdefault() pop() popitem() keys() values() item()
'''
import os
import pickle
from collections import MutableMapping

class PersistentDict(MutableMapping):

    def __init__(self, dirname):
        self.dirname = dirname
        try:
            os.mkdir(dirname)
        except OSError:
            pass

    def __setitem__(self, key, value):
        fullname = os.path.join(self.dirname, key)
        with open(fullname, 'w') as f:
            pickle.dump(value, f) 

    def __getitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            with open(fullname) as f:
                return pickle.load(f)
        except IOError:
            raise KeyError(key)

    def __delitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            os.remove(fullname)
        except OSError:
            raise KeyError(key)

    def __len__(self):
        return len(os.listdir(self.dirname))

    def __iter__(self):
        return iter(os.listdir(self.dirname))

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.dirname,
                               self.items())


if __name__=='__main__':
    d = PersistentDict('bharadwaj')
    d['homer'] = 'Doh!'
    d['bart'] = 'Cowabunga!'
    d['marge'] = 'Grrrr'
    d['lisa'] = 'oh Bart!'
    d['maggie'] = 'Suckling noises'
