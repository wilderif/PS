# BOJ_1719
# 택배

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    INF = 10 ** 9
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    next = [['-' for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if graph[a][b] > c:
            graph[a][b] = c
            graph[b][a] = c
            next[a][b] = b
            next[b][a] = a
    
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    next[i][j] = next[i][k]

    for i in range(1, n + 1):
        print(*next[i][1:])


if __name__ == "__main__":
    main()
