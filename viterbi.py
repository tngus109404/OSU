from collections import defaultdict
from heapq import *


def new_longest(n,edges):
    my_order, nodes = order(n, edges)
    best = {}
    length = 0
    back = None
    distance = defaultdict(int)

    for node in my_order:
        for i in nodes[node]:
            if distance[i] + 1 > distance[node]:
                distance[node] = distance[i] + 1
                best[node] = i

                if length < distance[node]:
                    length = distance[node]
                    back = node

    return (length, solution(back,best))
def longest(n,edges):
    my_order, nodes = order(n, edges)
    best = {}
    length = 0
    back = None
    distance = defaultdict(int)

    for node in my_order:
        for i in nodes[node]:
            if distance[i] + 1 > distance[node]:
                distance[node] = distance[i] + 1
                best[node] = i

                if length < distance[node]:
                    length = distance[node]
                    back = node

    return (length, solution(back,best))

def solution(node,best):
    if node not in best: return [node]
    return solution(best[node],best) + [node]

def order(n,edges):
    def visit(v):
        if v in visited:
            return
        visited.add(v)
        for u in child[v]:
            visit(u)
        output.append(v)


    graph = defaultdict(list)
    child = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        child[v].append(u)

    nodes = range(n)
    visited = set()
    output = []
    for a in nodes:
        visit(a)

    return output, child


# # print(longest(20000, tuples[:100])) #None
# print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
# print(new_longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
# print(new_order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
# print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])[0])

def generate_seq(k,length):
    import random
    random.seed(1)
    return [tuple(sorted(random.sample(range(k),2))) for _ in range(length)]
def rev_generate_seq(k,length):
    import random; random.seed(2)
    return [tuple(sorted(random.sample(range(k),2), reverse=True)) for _ in range(length)]
tuples = generate_seq(20000, 3300)
rev_tuples = rev_generate_seq(20000, 17700)
