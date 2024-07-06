# BOJ_17141
# 연구소 2

import sys
from collections import deque

inp = sys.stdin.readline


def bfs():
    global res
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    vis = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    for i in starting:
        q.append(i)
        vis[i[0]][i[1]] = 0
    while q:
        cur = q.popleft()
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and vis[nx][ny] == -1:
                vis[nx][ny] = vis[cur[0]][cur[1]] + 1
                q.append((nx, ny))
    ret = 0
    for i in range(n):
        for j in range(n):
            if vis[i][j] == -1 and not board[i][j]:
                return
        ret = max(ret, max(vis[i]))
    res = min(res, ret)


def backtracking(depth, start):
    if depth == m:
        bfs()
        return
    for i in range(start, len(can_v)):
        starting.append(can_v[i])
        backtracking(depth + 1, i + 1)
        starting.pop()


def main():
    global n, m, board, can_v, vis, res, starting
    n, m = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(n)]
    can_v = []
    starting = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                can_v.append((i, j))
                board[i][j] = 0
    res = 50 * 50
    backtracking(0, 0)
    if res == 50 * 50:
        print(-1)
        return
    print(res)


if __name__ == "__main__":
    main()
