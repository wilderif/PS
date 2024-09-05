# BOJ_17090
# 미로 탈출하기

import sys

inp = sys.stdin.readline


def dfs(starting):
    global res
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    stack = [starting]
    while stack:
        res += 1
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if i == 0 and board[nx][ny] == 'D':
                    stack.append((nx, ny))
                elif i == 1 and board[nx][ny] == 'U':
                    stack.append((nx, ny))
                elif i == 2 and board[nx][ny] == 'R':
                    stack.append((nx, ny))
                elif i == 3 and board[nx][ny] == 'L':
                    stack.append((nx, ny))


def main():
    global n, m, board, res
    n, m = map(int, inp().split())
    board = [inp().strip() for _ in range(n)]
    res = 0

    start = []
    for i in range(n):
        if board[i][0] == 'L':
            start.append((i, 0))
        if board[i][m - 1] == 'R':
            start.append((i, m - 1))


    for i in range(m):
        if board[0][i] == 'U':
            start.append((0, i))
        if board[n - 1][i] == 'D':
            start.append((n - 1, i))

    for i in start:
        dfs(i)
    print(res)


if __name__ == "__main__":
    main()
