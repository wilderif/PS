# BOJ_5719
# 거의 최단 경로

import sys
import heapq

inp = sys.stdin.readline


def dijkstra(graph, n, s):
    min_heap = [(0, s)]
    dist = [float("inf") for _ in range(n)]
    prev_path = [set() for _ in range(n)]
    dist[s] = 0

    while min_heap:
        cur_c, cur_v = heapq.heappop(min_heap)
        if cur_c != dist[cur_v]:
            continue

        for nxt_c, nxt_v in graph[cur_v]:
            cost = cur_c + nxt_c
            if dist[nxt_v] < cost:
                continue
            if dist[nxt_v] == cost:
                prev_path[nxt_v].add((nxt_c, cur_v))
            else:
                prev_path[nxt_v].clear()
                prev_path[nxt_v].add((nxt_c, cur_v))

                dist[nxt_v] = cost
                heapq.heappush(min_heap, (cost, nxt_v))

    return dist, prev_path


def main():
    while True:
        n, m = map(int, inp().split())
        if n == 0 and m == 0:
            return
        s, d = map(int, inp().split())
        graph = [set() for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, inp().split())
            graph[u].add((p, v))

        _, prev_path = dijkstra(graph, n, s)

        stack = [d]
        while stack:
            cur = stack.pop()
            for pre_c, pre_v in prev_path[cur]:
                if (pre_c, cur) in graph[pre_v]:
                    graph[pre_v].remove((pre_c, cur))
                    stack.append(pre_v)

        dist, _ = dijkstra(graph, n, s)
        print(dist[d] if dist[d] != float("inf") else -1)


if __name__ == "__main__":
    main()
