def convertbin(d):
    blst = []
    curno = int(d)
    while curno > 1:
        print curno
        if curno%2 == 0:
            blst.append(str(0))
        elif curno%2 == 1:
            blst.append(str(1))
        curno = curno//2
        if curno == 1:
            blst.append(str(1))
    return ''.join(blst[::-1])

print convertbin(13)
         
        
