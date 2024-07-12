# BOJ_14284
# 간선 이어가기 2

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
        for nxt_v, nxt_c in graph[cur_v].items():
            cost = cur_c + nxt_c
            if cost < dist[nxt_v]:
                dist[nxt_v] = cost
                prev[nxt_v] = cur_v
                heapq.heappush(min_heap, (cost, nxt_v))
    return prev


def main():
    n, m = map(int, inp().split())
    graph = [{} for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if b not in graph[a] or graph[a][b] > c:
            graph[a][b] = c
            graph[b][a] = c
    s, t = map(int, inp().split())
    
    prev = dijkstra(graph, n, s)

    res = 0
    node = t
    while node != s:
        res += graph[node][prev[node]]
        node = prev[node]
    print(res)


if __name__ == "__main__":
    main()
