# BOJ_17616
# 등수 찾기

import sys

inp = sys.stdin.readline


def dfs(graph, start):
    vis = [False for _ in range(n + 1)]
    stack = [start]
    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if vis[nxt]:
                continue
            vis[nxt] = True
            stack.append(nxt)

    return vis.count(True)


def main():
    global n
    n, m, x = map(int, inp().split())
    graph_1 = [[] for _ in range(n + 1)]
    graph_2 = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        graph_1[a].append(b)
        graph_2[b].append(a)

    depth_1 = dfs(graph_1, x)
    depth_2 = dfs(graph_2, x)

    print(1 + depth_2, n - depth_1)


if __name__ == "__main__":
    main()
