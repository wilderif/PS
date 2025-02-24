# BOJ_1854
# K번째 최단경로 찾기

import sys
import heapq

inp = sys.stdin.readline


def dijkstra(graph, n, k):
    min_heap = [(0, 1)]
    dist = [[] for _ in range(n + 1)]
    heapq.heappush(dist[1], 0)

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if cur_c > -dist[cur_v][0]:
            continue

        for nxt_c, nxt_v in graph[cur_v]:
            cost = cur_c + nxt_c

            if len(dist[nxt_v]) == k:
                if cost >= -dist[nxt_v][0]:
                    continue
                else:
                    heapq.heappushpop(dist[nxt_v], -cost)
            else:
                heapq.heappush(dist[nxt_v], -cost)
            heapq.heappush(min_heap, (cost, nxt_v))

    return dist


def main():
    n, m, k = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        graph[a].append((c, b))

    dist = dijkstra(graph, n, k)

    for i in range(1, n + 1):
        print(-dist[i][0] if len(dist[i]) == k else -1)


if __name__ == "__main__":
    main()
