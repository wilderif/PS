# BOJ_9370
# 미확인 도착지

import sys
import heapq

inp = sys.stdin.readline


def dijkstra(graph, n, start):
    dist = [float('inf') for _ in range(n + 1)]
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
                heapq.heappush(min_heap, (cost, nxt_v))
    return dist


def main():
    T = int(inp())
    for _ in range(T):
        n, m, t = map(int, inp().split())
        s, g, h = map(int, inp().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, d = map(int, inp().split())
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        s_dist = dijkstra(graph, n, s)
        inter = None
        if s_dist[g] > s_dist[h]:
            inter = g
        else:
            inter = h
        inter_dist = dijkstra(graph, n, inter)
        res = []
        for _ in range(t):
            x = int(inp())
            if s_dist[x] == float('inf'):
                continue
            if s_dist[x] == s_dist[inter] + inter_dist[x]:
                res.append(x)
        print(*sorted(res))

                
if __name__ == "__main__":
    main()
