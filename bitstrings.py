def fib(a,fibs={0:1, 1:2}):
    if a not in fibs:
        fibs[a]=fib(a-1)+fib(a-2)
    return fibs[a]

def num_no(a):
    return fib(a)

def num_yes(a):
    k=1
    for i in range(a):
       k*=2
    return k-fib(a)
