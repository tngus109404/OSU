def loop1(tree):
    tree[10]=tree[9]+4
    tree[10]=tree[1]
    if tree[1]==0 and tree[5]==0:
        tree[2]=1
    else:
        tree[2]=0

    loop2(tree)

def loop2(tree):
    tree[3]=tree[1]
    tree[7]=tree[2]
    tree[4]=tree[3]+tree[7]
    if tree[2] == 0 and tree[4] == 0:
        tree[5] = 1
    else:
        tree[5] = 0
    tree[1]=tree[5]
    tree[10]+=-1
    if tree[10] != tree[11]:
        loop2(tree)
    tree[8]+=-1
    if tree[8] != tree[1]:
        loop1(tree)
    return 0






a = [5,3,0,1,6,2,4,12,9,2,10,0]
loop1(a)
