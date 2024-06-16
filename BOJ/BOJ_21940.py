# BOJ_21940
# 가운데에서 만나기

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = map(int, inp().split())
        if graph[a][b] > t:
            graph[a][b] = t
    k = int(inp())
    arr = list(map(int, inp().split()))

    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    cur_min = float('inf')
    res = []
    for node in range(1, n + 1):
        tmp = 0
        for i in arr:
            tmp = max(tmp, graph[i][node] + graph[node][i])
        if tmp < cur_min:
            cur_min = tmp
            res = [node]
        elif tmp == cur_min:
            res.append(node)
    
    print(*sorted(res))


if __name__ == "__main__":
    main()
