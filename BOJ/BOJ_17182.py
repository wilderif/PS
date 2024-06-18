# BOJ_17182
# 우주 탐사선

import sys

inp = sys.stdin.readline


def backtracking(node, cost, cnt):
    global res
    if cnt == n:
        res = min(res, cost)
        return
    for i in range(n):
        if not vis[i]:
            vis[i] = 1
            backtracking(i, cost + graph[node][i], cnt + 1)
            vis[i] = 0


def main():
    global res, n, graph, vis
    n, k = map(int, inp().split())
    graph = [list(map(int, inp().split())) for _ in range(n)]
    
    for p in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][p] + graph[p][j]:
                    graph[i][j] = graph[i][p] + graph[p][j]
    
    res = float("inf")
    vis = [0 for _ in range(n)]
    vis[k] = 1
    backtracking(k, 0, 1)
    print(res)


if __name__ == "__main__":
    main()
