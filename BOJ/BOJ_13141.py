# BOJ_13141
# Ignition

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    inf = 10 ** 9
    graph = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    graph_max = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        s, e, l = map(int, inp().split())
        if graph[s][e] > l:
            graph[s][e] = l
            graph[e][s] = l
        if graph_max[s][e] < l:
            graph_max[s][e] = l
            graph_max[e][s] = l
    
    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    res = inf
    for k in range(1, n + 1):
        k_tmp = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if graph_max[i][j]:
                    k_tmp = max(k_tmp, (graph[k][i] + graph[k][j] + graph_max[i][j]) / 2)
        res = min(res, k_tmp)
    print(res)


if __name__ == "__main__":
    main()
