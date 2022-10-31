def best(i,items):
    n=len(items)
    back={}
    bk=[0]*n

    def b(i,best={0:0}):
        if i in best:
            return best[i]
        best[i]=0
        for j in range(n):
            if i >= items[j][0]:
                temp=b(i - items[j][0]) + items[j][1]
                if temp > best[i]:
                    back[i]=j
                    best[i]=temp

        return best[i]


    return b(i), solution(i,back,items,bk)


def solution(i,back,items,bk):
    if i < 1:
        return -1
    idx=items.index((items[back[i]][0],items[back[i]][1]))
    bk[idx]+=1
    solution(i-items[back[i]][0], back, items, bk)
    return bk