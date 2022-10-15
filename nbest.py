from heapq import *

def nbesta(a,b):
    c=[]
    for i in a:
        for j in b:
            c.append((i,j))
    c.sort(key=lambda x : (x[0]+x[1] , x[1]))
    n=len(a)
    return c[:n]

def nbestb(a,b):
    c = []
    for j in b:
        for i in a:
            c.append((i,j))
    d=[]
    for k in range(len(a)):
        d.append(qselect(k+1,c))

def nbestc(a,b):
    a.sort()
    b.sort()
    h=[]
    d=[]
    for m,k in enumerate(b):
        h.append((a[0]+b[m],m,(a[0],k),(0,m)))
    heapify(h)
    for jang in range(len(a)):
        c=heappop(h)
        d.append(c[2])
        i=c[3][0]
        j=c[3][1]
        if i <= len(a):
            new=(a[i+1]+b[j],j,(a[i+1],b[j]),(i+1,j))
            heappush(h, new)
    return d

def qselect(i:int, a:list)->int:
    if a == []:
        return []
    pivot=a[0]
    left = [x for x in a if sum(x) < sum(pivot)]
    len_left = len(left)
    if len_left == i - 1:
        return pivot
    elif len_left < i - 1:
        right = [x for x in a[1:] if sum(x) >= sum(pivot)]
        return qselect(i - len_left - 1, right)
    else:
        return qselect(i,left)


