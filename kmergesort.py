from heapq import *
INF = float("inf")
def kmergesort(tree,k):
    lt = len(tree)
    sum_partition=[]
    if lt <= 1:
        return tree
    for i in range(k):
        c = lt * i // k
        partition = kmergesort(tree[c:(lt * (i + 1)) // k], k)
        sum_partition += partition
    result = kmergesorted(sum_partition, k)
    return result

def kmergesorted(tree, k):
    lt = len(tree)
    if lt <= 1:
        return tree
    new,idx,h=[],[],[]
    heapify(h)
    j=0
    og_idx=[]
    if lt < k:
        lenth=lt
    else:
        lenth=k
    for i in range(lenth):
        c = lt * i // lenth
        idx.append(c+i)
        og_idx.append(c)
        heappush(h,(tree[c],c))
    for i in range(lt):
        if j in og_idx[1:]:
            new.append((INF,INF))
            new.append((tree[i],j))
        else:
            new.append((tree[i],j))
        j+=1
    new.append((INF,INF))
    rt=[]
    jj=[]
    heapify(jj)
    if lt<k:
        hu=lt
        for i in range(hu):
            heappush(jj, new[idx[i]])
        for i in range(hu):
            o2o2=heappop(jj)
            rt.append(o2o2[0])
    else:
        hu=lt+k
        for i in range(hu):
            if len(jj)<k:
                heappush(jj,new[idx[i]])
            else:
                a=heappop(jj)
                rt.append(a[0])
                index=og_idx.index(a[1])
                idx[index]+=1
                if og_idx[index]+1 in og_idx:
                    og_idx[index]=INF
                else:
                    og_idx[index]+=1

                heappush(jj,new[idx[index]])

    return rt
