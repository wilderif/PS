# BOJ_24479
# 알고리즘 수업 - 깊이 우선 탐색 1

import sys

sys.setrecursionlimit(10**6)
inp = sys.stdin.readline


def dfs(v, e, r):
    global order
    v[r] = order
    order += 1
    for node in e[r]:
        if v[node] != 0:
            continue
        dfs(v, e, node)


def dfs_2(graph, vis, start):
    stack = [start]
    order = 1
    while stack:
        cur = stack.pop()
        if not vis[cur]:
            vis[cur] = order
            order += 1
            for node in reversed(graph[cur]):
                if not vis[node]:
                    stack.append(node)


def main():
    global vis, order
    n, m, r = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    vis = [0 for _ in range(n + 1)]
    order = 1

    for _ in range(m):
        u, v = map(int, inp().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort()

    dfs(vis, graph, r)
    # dfs_2(graph, vis, r)

    for i in range(1, n + 1):
        print(vis[i])


if __name__ == "__main__":
    main()
