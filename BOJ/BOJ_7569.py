# BOJ_7569
# 토마토

import sys
from collections import deque


def main():
    dx = (1, 0, 0, -1, 0, 0)
    dy = (0, 1, 0, 0, -1, 0)
    dz = (0, 0, 1, 0, 0, -1)
    m, n, h = map(int, sys.stdin.readline().split())
    arr = list()
    for _ in range(h):
        tmp = list()
        for _ in range(n):
            tmp.append(list(map(int, sys.stdin.readline().split())))
        arr.append(tmp)
    vis = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    
    q = deque()
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if arr[k][j][i] == 1:
                    q.append((k, j, i))
                    vis[k][j][i] = 0

    while q:
        cur = q.popleft()
        cur_time = vis[cur[0]][cur[1]][cur[2]]
        for d in range(6):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            nz = cur[2] + dz[d]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if arr[nx][ny][nz] != -1 and vis[nx][ny][nz] == -1:
                    q.append((nx, ny, nz))
                    vis[nx][ny][nz] = cur_time + 1

    res = 0    
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if vis[k][j][i] == -1 and arr[k][j][i] != -1:
                    print(-1)
                    return
                else:
                    res = max(res, vis[k][j][i])
    print(res)


if __name__ == "__main__":
    main()
