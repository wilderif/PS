# BOJ_2211
# 네트워크 복구

import sys
import heapq

inp = sys.stdin.readline


def dijkstra(graph, n, start):
    dist = [float('inf') for _ in range(n + 1)]
    prev = [0 for _ in range(n + 1)]
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] != cur_c:
            continue
        for nxt_v, nxt_c in graph[cur_v]:
            cost = cur_c + nxt_c
            if cost < dist[nxt_v]:
                dist[nxt_v] = cost
                prev[nxt_v] = cur_v
                heapq.heappush(min_heap, (cost, nxt_v))
    return prev


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    prev = dijkstra(graph, n, 1)
    print(n - 1)
    for i in range(2, n + 1):
        print(i, prev[i])


if __name__ == "__main__":
    main()
