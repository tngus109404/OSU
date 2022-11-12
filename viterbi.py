from collections import defaultdict
from heapq import *

def longest(n,edges):

    my_order = order(n,edges)
    print(f"my_order={my_order}")
    graph = defaultdict(list)
    pointer = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        pointer[v].append(u)
    print(graph)
    print(pointer[7])
    path = 0


def order(n, edges):
    if edges == []:
        output=[]
        for i in range(n):
            output.append(i)
        return output

    graph = defaultdict(list)
    pointer = defaultdict(list)
    h=[]
    output=[]

    for u,v in edges:
        graph[u].append(v)
        pointer[v].append(u)
    for u in edges:
        if pointer[u[0]] == []:
            heappush(h,u)
            if u[0] not in output:
                output.append(u[0])

    while h != []:
        u,v = heappop(h)
        pointer[v].remove(u)
        if pointer[v] == [] :
            for j in graph[v]:
                heappush(h,(v,j))
            if v not in output:
                    output.append(v)

    if len(output) < n:
        return
    else:
        return output

def professor(n, edges):

    def visit(v):
        if v in visited:
            return
        visited.add(v)
        for u in prereqs[v]:
            visit(u)
        output.append(v)

    graph=defaultdict(list)
    prereqs=defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        prereqs[v].append(u)

    nodes = range(n)
    output=[]
    visited = set()
    for v in nodes:
        print(v)
        visit(v)
    return output


#
# print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
# print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
