from bisect import bisect

def find(tree, x, k):
    mid=bisect(tree,x)
    lp = mid-1
    rp = mid
    num=0
    c=[]
    while (lp > 0 or rp < len(tree)) and num <k :
        if lp==0 or  (rp<len(tree) and abs(round(x-tree[lp],2)) > abs(round(x-tree[rp],2))):
            c.append(tree[rp])
            rp+=1
        else:
            c.insert(0,tree[lp])
            lp-=1
        num+=1

    return c
