# BOJ_1238
# 파티

import sys
import heapq

inp = sys.stdin.readline


def dijkstra(graph, n, start):
    min_heap = [(0, start)]
    dist = [10 ** 9 for _ in range(n + 1)]
    dist[start] = 0
    
    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if cur_c != dist[cur_v]:
            continue
        for nxt_v, nxt_c in graph[cur_v]:
            if dist[nxt_v] > cur_c + nxt_c:
                dist[nxt_v] = cur_c + nxt_c
                heapq.heappush(min_heap, (cur_c + nxt_c, nxt_v))

    return dist


def main():
    n, m, x = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    graph_reverse = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        graph[a].append((b, c))
        graph_reverse[b].append((a, c))
    
    dist_1 = dijkstra(graph, n, x)
    dist_2 = dijkstra(graph_reverse, n, x)

    res = 0
    for i in range(1, n + 1):
        res = max(res, dist_1[i] + dist_2[i])

    print(res)


if __name__ == "__main__":
    main()
