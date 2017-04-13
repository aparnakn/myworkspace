def bintodec(d):
    dec = 0
    d = (d.split()).reverse()
    for idx,items in d[::-1]:
        print items
        dec+= int(items*(2**d.index(items)))
        print dec
    return dec

print bintodec('1101')
