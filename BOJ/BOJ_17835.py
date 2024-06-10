# BOJ_17835
# 면접보는 승범이네

import sys
import heapq

inp = sys.stdin.readline

def dijkstra(graph, n, start):
    dist = [float('inf') for _ in range(n + 1)]
    min_heap = []
    for i in start:
        dist[i] = 0
        heapq.heappush(min_heap, (0, i))

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] != cur_c:
            continue

        for nxt_v, nxt_c in graph[cur_v].items():
            if dist[nxt_v] > cur_c + nxt_c:
                dist[nxt_v] = cur_c + nxt_c
                heapq.heappush(min_heap, (cur_c + nxt_c, nxt_v))
    return dist


def main():
    n, m, k = map(int, inp().split())
    graph = [{} for _ in range(n + 1)]
    for _ in range(m):
        u, v, c = map(int, inp().split())
        if u not in graph[v] or graph[v][u] > c:
            graph[v][u] = c
    start_arr = list(map(int, inp().split()))
    
    dist = dijkstra(graph, n, start_arr)
             
    res_1, res_2 = 0, 0
    for i in range(n, 0, -1):
        if dist[i] >= res_2:
            res_2 = dist[i]
            res_1 = i
    print(res_1)
    print(res_2)


if __name__ == "__main__":
    main()
