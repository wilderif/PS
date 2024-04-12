# BOJ_1743
# 음식물 피하기

import sys
from collections import deque


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n, m, k = map(int, sys.stdin.readline().split())
    arr = [[False for _ in range(m)] for _ in range(n)]
    vis = [[True for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[a - 1][b - 1] = True
    
    res = 0
    for j in range(n):
        for i in range(m):
            if arr[j][i] and vis[j][i]:
                q = deque()
                q.append((j, i))
                vis[j][i] = False
                tmp = 1
                while q:
                    cur = q.popleft()
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] and vis[nx][ny]:
                                vis[nx][ny] = False
                                q.append((nx, ny))
                                tmp += 1
                res = max(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
