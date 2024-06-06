# BOJ_11404
# 플로이드

import sys
import math

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    graph = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if graph[a][b] > c:
            graph[a][b] = c
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            for k in range(1, n + 1):
                if j == k:
                    continue
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print(0, end=' ')
            else:
                if graph[i][j] != math.inf:
                    print(graph[i][j], end=' ')
                else:
                    print(0, end=' ')
        print()


if __name__ == "__main__":
    main()
