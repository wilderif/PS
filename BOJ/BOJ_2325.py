# BOJ_2325
# 개코전쟁

import sys
import heapq

inp = sys.stdin.readline

def dijkstra(graph, n, start, v1, v2):
    dist = [10 ** 9 for _ in range(n + 1)]
    prev = [None for _ in range(n + 1)]
    dist[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if dist[cur_v] != cur_c:
            continue

        for nxt_v, nxt_c in graph[cur_v]:
            if (cur_v == v1 and nxt_v == v2) or (cur_v == v2 and nxt_v == v1):
                continue
            if dist[nxt_v] > cur_c + nxt_c:
                dist[nxt_v] = cur_c + nxt_c
                prev[nxt_v] = cur_v
                heapq.heappush(min_heap, (cur_c + nxt_c, nxt_v))

    return dist, prev


def main():
    n, m = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, z = map(int, inp().split())
        graph[x].append((y, z))
        graph[y].append((x, z))

    _, prev = dijkstra(graph, n, 1, 0, 0)
    path = []
    node = n
    while node != 1:
        path.append(node)
        node = prev[node]
    path.append(1)

    res = 0
    for i in range(len(path) - 1):
        dist, _ = dijkstra(graph, n, 1, path[i], path[i + 1])
        res = max(res, dist[n])
    
    print(res)


if __name__ == "__main__":
    main()
