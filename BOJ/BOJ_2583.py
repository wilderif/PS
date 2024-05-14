# BOJ_2583
# 영역 구하기

import sys
from collections import deque


def main():
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(n)] for _ in range(m)]
    vis = [[False for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
        for j in range(y_1, y_2):
            for i in range(x_1, x_2):
                arr[j][i] = 1

    res_1 = 0
    res_2 = []
    for j in range(m):
        for i in range(n):
            tmp = 0
            if not vis[j][i] and not arr[j][i]:
                vis[j][i] = True
                res_1 += 1
                tmp += 1
                q = deque()
                q.append((j, i))
                while q:
                    cur = q.popleft()
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < m and 0 <= ny < n:
                            if not vis[nx][ny] and not arr[nx][ny]:
                                vis[nx][ny] = True
                                tmp += 1
                                q.append((nx, ny))
                res_2.append(tmp)
    print(res_1)
    print(*sorted(res_2))


if __name__ == "__main__":
    main()
