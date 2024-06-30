# BOJ_17086
# 아기 상어 2

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    dx = (-1, -1, -1, 1, 1, 1, 0, 0)
    dy = (-1, 0, 1, -1, 0, 1, -1, 1)
    n, m = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(n)]
    vis = [[-1 for _ in range(m)] for _ in range(n)]

    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                q.append((i, j))
                vis[i][j] = 0

    while q:
        cur = q.popleft()
        for d in range(8):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] == -1:
                vis[nx][ny] = vis[cur[0]][cur[1]] + 1
                q.append((nx, ny))
    
    res = 0
    for i in vis:
        res = max(res, max(i))
    print(res)


if __name__ == "__main__":
    main()
