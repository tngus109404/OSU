def bsts(i, fibs={0:1, 1:1}):
    if i not in fibs:
        sum=0
        for id in range(i):
            sum+=bsts(id)*bsts(i-1-id)
        fibs[i]=sum
    return fibs[i]