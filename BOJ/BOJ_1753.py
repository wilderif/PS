# BOJ_1753
# 최단경로

import sys
import math
import heapq

inp = sys.stdin.readline


def main():
    v, e = map(int, inp().split())
    k = int(inp())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, inp().split())
        graph[a].append((c, b))
    
    min_heap = [(0, k)]
    dist = [math.inf for _ in range(v + 1)]
    dist[k] = 0

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] < cur_c:
            continue

        for nxt_c, nxt_v in graph[cur_v]:
            cost = nxt_c + cur_c
            if cost < dist[nxt_v]:
                dist[nxt_v] = cost
                heapq.heappush(min_heap, (cost, nxt_v))
    
    for i in range(1, v + 1):
        if dist[i] == math.inf:
            print("INF")
        else:
            print(dist[i])


if __name__ == "__main__":
    main()
