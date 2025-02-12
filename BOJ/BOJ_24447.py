# BOJ_24447
# 알고리즘 수업 - 너비 우선 탐색 4

import sys

inp = sys.stdin.readline


def bfs(vis, graph, start):
    ret = 0
    depth = 0
    order = 1
    queue = []
    queue.append(start)
    vis[start] = depth
    while queue:
        new_queue = []
        depth += 1
        for cur in queue:
            for nxt in graph[cur]:
                if vis[nxt] is False:
                    vis[nxt] = True
                    order += 1
                    ret += order * depth
                    new_queue.append(nxt)
        queue = new_queue

    return ret


def main():
    n, m, r = map(int, inp().split())
    graph = [[] for _ in range(n + 1)]
    vis = [False for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, inp().split())
        graph[u].append(v)
        graph[v].append(u)

    for adj in graph:
        adj.sort(reverse=True)

    res = bfs(vis, graph, r)

    print(res)


if __name__ == "__main__":
    main()
