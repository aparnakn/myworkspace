'''
lst = ['a', 'b', 'c', 'b', 'a', 'e', 'c']
print duplicates and no of duplicates
'''

def printdup(lst):
    dic = {}
    for item in lst:
        if item in dic:
            dic[item]+=1
        else:
           dic[item] = 1
    print [ (key, value) for key, value in dic.iteritems() if value > 1 ] 


printdup(['a', 'b', 'c', 'b', 'a', 'e', 'c'])
