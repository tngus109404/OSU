from priority_dict import priority_dict
from collections import defaultdict
INF = float("inf")
def shortest(n, edges):
    if edges ==[]:
        return None
    color = {}
    pri_queue=priority_dict()
    connect = defaultdict(list)
    weight = defaultdict(list)
    back =  defaultdict(int)
    pri_queue[0],color[0] = 0, "white"

    def solution(n,back):
        if n not in back: return [n]
        return solution(back[n], back) + [n]

    for node in edges: # O(E)
        from_node=node[0]
        to_node=node[1]
        node_weight=node[2]
        if from_node not in pri_queue :
            pri_queue.setdefault(from_node, INF)
        elif to_node not in pri_queue:
            pri_queue.setdefault(to_node, INF)
        connect[from_node].append(to_node)
        connect[to_node].append(from_node)
        color[from_node]="white"
        color[to_node]="white"
        weight[(from_node,to_node)]=node_weight
        weight[(to_node,from_node)]=node_weight
    while pri_queue != {}:
        v=pri_queue.pop_smallest()
        color[v[0]]="black"
        if v[1]==INF:
            return None
        elif v[0]==n-1:
            return v[1], solution(n-1,back)
        for u in connect[v[0]]:
            if color[u] == "white":
                if u in pri_queue:
                    if v[1] + weight[(v[0], u)] < pri_queue[u]:
                        pri_queue[u] = v[1] + weight[(v[0], u)]
                        back[u] = v[0]
                else:
                    pri_queue[u] = v[1] + weight[(v[0], u)]
                    back[u] = v[0]








# print(shortest(1000, [(0, 89, 10), (0, 221, 5), (0, 301, 20), (0, 331, 5), (0, 404, 16), (0, 728, 21), (0, 999, 27), (89, 451, 10), (89, 605, 5), (89, 728, 11), (89, 999, 16), (221, 236, 10), (221, 268, 9), (221, 382, 5), (221, 331, 5), (301, 331, 7), (301, 728, 8), (301, 999, 15), (331, 404, 7), (331, 473, 8), (331, 496, 10), (332, 534, 10), (331, 999, 30), (728, 996, 9), (996, 999, 5), (728, 999, 5)]))
# print(shortest(5, [(0,1,5), (0,2,3), (1,3,3), (1,2,1), (2,3,5),(2,4,10),(3,4,1)]))
# print(shortest(6, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (1,4,2),(3,4,3),(3,5,9),(4,5,7)]))
