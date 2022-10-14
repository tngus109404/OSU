from bisect import *
from heapq import *
def ksmallest(k, tree):
    lt = len(tree)
    h = []
    minV = []

    if lt//2 < k <= lt:
        for i in tree[:k]:
            h.append(i)
        heapify(h)
        for i in range(lt-k):
            if h[0]<tree[k+i]:
                a = heappop(h)
                heappush(h,tree[k+i])
                bs = bisect(minV, a)
                minV.insert(bs, a)
            else:
                minV.append(tree[k+i])

        for i in range(2*k-lt):
            a = heappop(h)
            minV.append(a)
        return minV

    elif k > lt:
        heapify(tree)
        for i in range(lt):
            a=heappop(tree)
            minV.append(a)
        return minV

    else:
        for i in range(k):
            h.append(tree[i])
        heapify(h)
        for i in tree[k:]:
            if h[0] < i:
                a=heappop(h)
                heappush(h,i)
                bs= bisect(minV, a)
                minV.insert(bs,a)
                minV=minV[:k]
            else:
                bs=bisect(minV,i)
                if bs < k:
                    minV.insert(bs,i)
                    minV=minV[:k]
        return minV


ksmallest(20, [10, 7, 23, 2, 9, 3, 7, 8, 11, 5, 7])
# == [2, 3, 5, 7, 7, 7, 8, 9, 10, 11, 23]
ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
# == [2,3,5,7]
ksmallest(3, range(1000000, 0, -1))
# == [1,2,3]
ksmallest(10, [10, 2, 9, 3, 7, 3, 9, 3, 7, 8, 11, 8, 11, 5, 7])
#== [2, 3, 3, 3, 5, 7, 7, 7, 8, 8]
