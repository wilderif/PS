# BOJ_24444
# 알고리즘 수업 - 너비 우선 탐색 1

import sys
from collections import deque

inp = sys.stdin.readline


def bfs(vis, graph, start):
    order = 1
    queue = deque()
    queue.append(start)
    vis[start] = order
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not vis[nxt]:
                order += 1
                vis[nxt] = order
                queue.append(nxt)


def main():
    n, m, r = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    vis = [0 for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, inp().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort()

    bfs(vis, graph, r)

    for i in range(1, n + 1):
        print(vis[i])


if __name__ == "__main__":
    main()
