# 야근_지수

import heapq


def solution(n, works):
    max_heap = []
    for i in works:
        heapq.heappush(max_heap, -i)

    while n:
        n -= 1
        tmp = heapq.heappop(max_heap)
        if tmp == 0:
            return 0

        heapq.heappush(max_heap, tmp + 1)

    res = 0
    for i in max_heap:
        res += i ** 2

    return res
