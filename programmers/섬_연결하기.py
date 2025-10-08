# 섬_연결하기

import heapq


def solution(n, costs):
    edges = [[] for _ in range(n)]
    for e in costs:
        edges[e[0]].append((e[2], e[1]))
        edges[e[1]].append((e[2], e[0]))

    min_heap = []

    vis = [False for _ in range(n)]
    vis[0] = True
    for e in edges[0]:
        heapq.heappush(min_heap, e)

    res = 0

    while min_heap:
        cur_cost, cur_node = heapq.heappop(min_heap)
        if vis[cur_node]:
            continue
        vis[cur_node] = True
        res += cur_cost
        for nxt_cost, nxt_node in edges[cur_node]:
            if vis[nxt_node]:
                continue
            heapq.heappush(min_heap, (nxt_cost, nxt_node))

    return res
