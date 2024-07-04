# BOJ_11562
# 백양로 브레이크

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        u, v, b = map(int, inp().split())
        if not b:
            graph[u][v] = 0
            graph[v][u] = 1
        if b:
            graph[u][v] = 0
            graph[v][u] = 0
    
    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    k = int(inp())
    for _ in range(k):
        s, e = map(int, inp().split())
        print(graph[s][e])
 

if __name__ == "__main__":
    main()
