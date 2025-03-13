# 이중우선순위큐

import heapq


def solution(operations):
    arr = []
    for el in operations:
        tmp = el.split(" ")
        arr.append((tmp[0], int(tmp[1])))

    min_heap = []
    max_heap = []
    check = {}

    for el in arr:
        if el[0] == "I":
            heapq.heappush(min_heap, el[1])
            heapq.heappush(max_heap, -el[1])
            if el[1] in check:
                check[el[1]] += 1
            else:
                check[el[1]] = 1
        else:
            tmp = 0
            if el[1] == -1:
                while min_heap:
                    tmp = heapq.heappop(min_heap)
                    if check[tmp]:
                        break
            else:
                while max_heap:
                    tmp = -heapq.heappop(max_heap)
                    if check[tmp]:
                        break
            if tmp in check and check[tmp]:
                check[tmp] -= 1

    res = [0, 0]
    while max_heap:
        tmp = -heapq.heappop(max_heap)
        if check[tmp]:
            res[0] = tmp
            res[1] = tmp
            break
    while min_heap:
        tmp = heapq.heappop(min_heap)
        if check[tmp]:
            res[1] = tmp
            break

    return res
