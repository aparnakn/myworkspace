'''
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

b = [[1,4,7], [2,5,8], [3,6,9]]
'''

def transpose(a):
    b = [[0,0,0], [0,0,0], [0,0,0]]
    for i, items in enumerate(a):
        for j in range(len(items)):
            b[i][j] =  a[j][i]
    return b

print transpose([[1,2,3],
     [4,5,6],
     [7,8,9]]),
     

