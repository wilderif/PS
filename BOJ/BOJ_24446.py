# BOJ_24446
# 알고리즘 수업 - 너비 우선 탐색 3

import sys

inp = sys.stdin.readline


def bfs(vis, graph, start):
    depth = 0
    queue = []
    queue.append(start)
    vis[start] = depth
    while queue:
        new_queue = []
        depth += 1
        for cur in queue:
            for nxt in graph[cur]:
                if vis[nxt] == -1:
                    vis[nxt] = depth
                    new_queue.append(nxt)
        queue = new_queue


def main():
    n, m, r = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    vis = [-1 for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, inp().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort(reverse=True)

    bfs(vis, graph, r)

    for i in range(1, n + 1):
        print(vis[i])


if __name__ == "__main__":
    main()
