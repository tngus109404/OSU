def best(w,items):
    ori=[]
    new=[]
    new_items=[]
    for a,i in enumerate(items):
        new.append(((i[1]/i[0],-a),i))
        ori.append((i,a))
    new.sort(reverse=True)
    # print(new)
    # for i in range(len(new)-1):
    #     if new[i][0][0]==new[i+1][0][0]:
    #         print(new)
    #         new[i],new[i+1]=new[i+1],new[i]
    # print(f"new={new}")
    for i in new:
        new_items.append(i[1])
    items=new_items
    b={}
    back={}
    b[0,0]=0
    for x in range(w+1):
        for i in range(len(items)+1):
            if x == 0 or i == 0:
                b[x,i]=0
            else:
                big = 0
                for j in range(items[i-1][2]+1):
                    if x >= j*(items[i-1][0]):
                        c = b[x - (j * (items[i - 1][0])), i-1] + j * items[i - 1][1]
                        if big < c:
                            if c not in back:
                                back[c]=i
                        big=max(big, c)
                b[x,i]=big
    print(b[w, len(items)], solution(b[w, len(items)], back, w, items, ori))
    return b[w,len(items)],solution(b[w,len(items)],back,w,items,ori)

def solution(rt,back,w,items,ori):
    kkk=[]
    last=[0]*len(items)
    ret = [0]*len(items)
    new_ret=[]
    while rt>0:
        ret[back[rt]-1]+=1
        rt=rt-items[back[rt]-1][1]
    for h in range(len(ret)):
        new_ret.append((h,ret[h]))
    for i in range(len(items)):
        for j in range(len(ori)):
            if items[i]==ori[j][0]:
                kkk.append(j)
    abc=0
    for i in kkk:
        last[i]=ret[abc]
        abc+=1
    return last

# best(10,[(6,6,10),(5,4,10)])
# best(3, [(2, 4, 2), (3, 5, 3)]) #(5, [0, 1])
# best(7, [(2, 4, 2), (3, 5, 3)]) #(13, [2, 1])
best(10, [(1, 5, 1),(2,11,3), (1, 5, 0),(1,5,3)]) #(15, [2, 1])
# best(3, [(1, 5, 1), (1, 5, 3)]) #(15, [1, 2])
# best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]) #(130, [6, 4, 1])
# best(92, [(1, 6, 6),(6,15,9), (6, 15, 7), (8, 9, 2),(8,9,3), (2, 4, 7), (2, 20, 2)]) #(236, [6, 7, 3, 7, 2])

#
# a=best(3, [(2, 4, 2), (3, 5, 3)]) == (5, [0, 1])
# print(a)
# a=best(7, [(2, 4, 2), (3, 5, 3)]) ==(13, [2, 1])
# print(a)
# a=best(3, [(1, 5, 2), (1, 5, 3)]) ==(15, [2, 1])
# print(a)
# a=best(3, [(1, 5, 1), (1, 5, 3)]) ==(15, [1, 2])
# print(a)
# a=best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]) ==(130, [6, 4, 1])
# print(a)
# a=best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])==(236, [6, 7, 3, 7, 2])
# print(a)

