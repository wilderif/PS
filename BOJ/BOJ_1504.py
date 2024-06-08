# BOJ_1504
# 특정한 최단 경로

import sys
import heapq

inp = sys.stdin.readline


def dijkstra(n, graph, start):
    dist = [10 ** 9 for _ in range(n + 1)]
    dist[start] = 0
    min_heap = [(0, start)]
    
    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] != cur_c:
            continue
        
        for nxt_v, nxt_c in graph[cur_v].items():
            if nxt_c + cur_c < dist[nxt_v]:
                dist[nxt_v] = nxt_c + cur_c
                heapq.heappush(min_heap, (nxt_c + cur_c, nxt_v))
    
    return dist


def main():
    n, e = map(int, inp().split())
    graph = [{} for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, inp().split())
        if b not in graph[a] or graph[a][b] > c:
            graph[a][b] = c
            graph[b][a] = c
    v1, v2 = map(int, inp().split())

    start_v1 = dijkstra(n, graph, v1)
    start_v2 = dijkstra(n, graph, v2)
    res = min(start_v1[1] + start_v1[v2] + start_v2[n], start_v2[1] + start_v1[v2] + start_v1[n])

    if res >= 10 ** 9:
        print(-1)
    else:
        print(res)


if __name__ == "__main__":
    main()
