def find(tree):
    tree.sort()
    c = []
    for i in tree:
        first=tree.index(i)
        for j in tree[first+1:]:
            c.append((i,j,i+j))
    g=[]
    for i in range(len(c)):
        if c[i][2] in tree:
            g.append(c[i])
    return g


