def pairsSum(a):
    pairs = []
    nump = 0
    for i, iitems in enumerate(a):
        print iitems
        for jitems in a[i+1:]:
            print a[i+1:]
            sumk = iitems+jitems
            if sumk in a and sumk != iitems and sumk != jitems:
                pairs.append((iitems, jitems))
                nump+=1
                    
    return pairs

print pairsSum([10, 9, 3, 8, 0, 4, 10, 5, -10, -3]) 
