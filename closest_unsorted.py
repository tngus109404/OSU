import random

def find(tree, x, k):
    d=[]
    for i in range(len(tree)):
        d.append((abs(round(x-tree[i],1))))
    k_value = qselect(k,d)
    r = []
    i,j =0,0
    while i < len(d) and j<k:
        if d[i] <= k_value:
            r.append(tree[i])
            j+=1
        i+=1
    return r

def qselect(i:int, a:list)->int:
    if a == []:
        return []
    pivot = a[0]

    left = [x for x in a if x < pivot]
    len_left = len(left)
    if len_left == i - 1:
        return pivot
    elif len_left < i - 1:
        right = [x for x in a[1:] if x >= pivot]
        return qselect(i - len_left - 1, right)
    else:
        return qselect(i,left)



# find([4,1,3,2,7,4], 5.2, 2)#    returns   [4,4]
# find([4,1,3,2,7,4], 6.5, 3)#	returns   [4,7,4]
# find([5,3,4,1,6,3], 3.5, 2)#	returns   [3,4]