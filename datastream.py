import random

random.seed(10)
import heapq


def ksmallest(k, l):  # slow
    heap = []
    for i, x in enumerate(l):
        if i < k:
            heapq.heappush(heap, -x)
        elif -x > heap[0]:
            heapq.heapreplace(heap, -x)

    return sorted([-x for x in heap])


def ksmallest2(k, l):  # ~66% faster than the above
    l = iter(l)
    heap = []
    for _ in range(k):  # k << n, so no need to try ... except
        heap.append(-next(l))
    heapq.heapify(heap)
    for x in l:
        if -x > heap[0]:
            heapq.heapreplace(heap, -x)
    return sorted([-x for x in heap])


if __name__ == "__main__":
    # print(ksmallest(20, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    # print(ksmallest(3, range(1000000, 0, -1)))
    #
    l = [random.randint(0, 100) for r in range(200)]
    print(l)
    print(ksmallest(6, l))
    # l.sort()
    # print(l)
