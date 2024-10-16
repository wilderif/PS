# BOJ_11967
# 불켜기

import sys
from collections import deque

inp = sys.stdin.readline


def check_move(a, b, q):
    flag = False
    for d in range(4):
        nx, ny = a + dx[d], b + dy[d]
        if 1 <= nx <= n and 1 <= ny <= n:
            if used[nx][ny]:
                used[a][b] = True
                q.append((a, b))
                flag = True
                break
    if flag:
        tmp_q = deque()
        tmp_q.append((a, b))
        while tmp_q:
            x, y = tmp_q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if not used[nx][ny] and board[nx][ny]:
                        used[nx][ny] = True
                        tmp_q.append((nx, ny))
                        q.append((nx, ny))

    

def switch_on(x, y, q):
    global res
    for a, b in switch[x][y]:
        if not board[a][b]:
            board[a][b] = True
            res += 1
            check_move(a, b, q)


def bfs():
    q = deque()
    q.append((1, 1))

    while q:
        x, y = q.popleft()
        switch_on(x, y, q)


def main():
    global dx, dy, n, m, switch, board, used, res

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n, m = map(int, inp().split())
    switch = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        x, y, a, b = map(int, inp().split())
        switch[x][y].append((a, b))
    
    board = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    board[1][1] = True

    used = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    used[1][1] = True

    res = 1

    bfs()
    print(res)


if __name__ == "__main__":
    main()
