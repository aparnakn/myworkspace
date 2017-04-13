def equilibriumPoint(arr):
    if len(arr) == 1:
        return 1
    else:
        for i in range(1, len(arr)):
            print "i=%d" % i
            suma, sumb = 0, 0
            for items in arr[:i-1]:
                print arr[:i-1]
                suma+=items
            for items in arr[i+1:]:
                print arr[i+1:]
                sumb+=items
            if suma == sumb:
                return i+1

print equilibriumPoint([10, 5, 3, 5, 2, 2, 6, 8])
