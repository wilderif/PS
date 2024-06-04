# BOJ_11403
# 경로 찾기

import sys

inp = sys.stdin.readline


def dfs(graph, res, n, cur, node):
    for i in range(n):
        if graph[node][i] and not res[cur][i]:
            res[cur][i] = 1
            dfs(graph, res, n, cur, i)


def main():
    n = int(inp())
    graph = [list(map(int, inp().split())) for _ in range(n)]
    
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dfs(graph, res, n, i, i)

    for line in res:
        print(*line)


if __name__ == "__main__":
    main()
