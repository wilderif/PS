# BOJ_14940
# 쉬운 최단거리

import sys
from collections import deque


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n, m = map(int, sys.stdin.readline().split())
    arr = list()
    start = None
    vis = [[-1 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if arr[-1][j] == 2:
                start = (i, j)
            if arr[-1][j] == 0:
                vis[i][j] = 0
    q = deque()
    q.append(start)
    vis[start[0]][start[1]] = 0

    while q:
        cur = q.popleft()
        cur_time = vis[cur[0]][cur[1]]
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] == -1:
                vis[nx][ny] = cur_time + 1
                q.append((nx, ny))
    for v in vis:
        print(*v)


if __name__ == "__main__":
    main()
