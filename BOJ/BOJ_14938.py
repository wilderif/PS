# BOJ_14938
# 서강그라운드

import sys

inp = sys.stdin.readline


def main():
    n, m, r = map(int, inp().split())
    arr = [0] + list(map(int, inp().split()))
    graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(r):
        a, b, i = map(int, inp().split())
        if graph[a][b] > i:
            graph[a][b] = i
            graph[b][a] = i
    
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    res = 0
    for i in range(1, n + 1):
        tmp = 0
        for j in range(1, n + 1):
            if graph[i][j] <= m:
                tmp += arr[j]
        res = max(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
