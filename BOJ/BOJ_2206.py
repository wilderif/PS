# BOJ_2206
# 벽 부수고 이동하기

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n, m = map(int, inp().split())
    board = [list(map(int, list(inp().rstrip()))) for _ in range(n)]
    vis = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    
    q = deque()
    q.append((0, 0, 0, 1))
    vis[0][0][0] = 1

    while q and vis[n - 1][m - 1][0] == -1 and vis[n - 1][m - 1][1] == -1:
        cur = q.popleft()
        for d in range(4):
            nx, ny = cur[0] + dx[d], cur[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if cur[2] == 0:
                    if board[nx][ny] == 0:
                        if vis[nx][ny][0] == -1:
                            vis[nx][ny][0] = cur[3] + 1
                            q.append((nx, ny, 0, cur[3] + 1))
                    else:
                        if vis[nx][ny][1] == -1:
                            vis[nx][ny][1] = cur[3] + 1
                            q.append((nx, ny, 1, cur[3] + 1))
                else:
                    if board[nx][ny] == 0:
                        if vis[nx][ny][1] == -1:
                            vis[nx][ny][1] = cur[3] + 1
                            q.append((nx, ny, 1, cur[3] + 1))
    
    if vis[n - 1][m - 1][0] == -1 and vis[n - 1][m - 1][1] == -1:
        print(-1)
        return
    
    if vis[n - 1][m - 1][0] != -1:
        print(vis[n - 1][m - 1][0])
    else:
        print(vis[n - 1][m - 1][1])


if __name__ == "__main__":
    main()
