# BOJ_11780
# 플로이드 2

import sys
import math

inp = sys.stdin.readline


def get_path(start, end, dist):
    ret = []
    node = start
    ret.append(start)
    while node != end:
        ret.append(dist[node][end])
        node = dist[node][end]
    return ret


def main():
    n = int(inp())
    m = int(inp())
    dist = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
    nxt = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, inp().split())
        if dist[a][b] > c:
            dist[a][b] = c
            nxt[a][b] = b

    for i in range(1, n + 1):
        dist[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == math.inf:
                print(0, end=' ')
            else:
                print(dist[i][j], end=' ')
        print()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or dist[i][j] == math.inf:
                print(0)
            else:
                tmp = get_path(i, j, nxt)
                print(len(tmp), *tmp)


if __name__ == "__main__":
    main()
