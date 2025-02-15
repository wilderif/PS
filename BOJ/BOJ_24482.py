# BOJ_24482
# 알고리즘 수업 - 깊이 우선 탐색 4

import sys

sys.setrecursionlimit(10**6)
inp = sys.stdin.readline


def dfs(start, depth):
    for nxt in graph[start]:
        if vis[nxt] == -1:
            vis[nxt] = depth
            dfs(nxt, depth + 1)


def main():
    global graph, vis
    n, m, r = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, inp().split())
        graph[u].append(v)
        graph[v].append(u)
    for e in graph:
        e.sort(reverse=True)

    vis = [-1 for _ in range(n + 1)]
    vis[r] = 0
    dfs(r, 1)

    for i in range(1, n + 1):
        print(vis[i])


if __name__ == "__main__":
    main()
