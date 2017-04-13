def pick(p, i):
    p1 = list(p)
    c = p1.pop(i)
    return c, p1

def join(c, perms):
    return [c+s for s in perms]

def perm(str):
    pool = tuple(str)
    if len(pool) == 2:
        return [pool[0]+pool[1], pool[1]+pool[0]]
    if len(pool) == 1:
	return [pool[0]]

    lst = []
    for i in range(len(pool)):
        c, p1 = pick(pool, i)
        lst.extend(join(c, perm(p1)))
 
    return lst

print set(perm('abcd'))
