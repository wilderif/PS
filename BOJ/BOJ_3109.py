# BOJ_3109
# 빵집

import sys

inp = sys.stdin.readline


def dfs(x, y):
    global board
    if y == m - 1:
        return True

    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == ".":
            board[nx][ny] = "x"
            if dfs(nx, ny):
                return True
    return False


def main():
    global dx, dy, n, m, board
    dx = (-1, 0, 1)
    dy = (1, 1, 1)
    n, m = map(int, inp().split())
    board = [list(inp().strip()) for _ in range(n)]

    res = 0
    for i in range(n):
        if dfs(i, 0):
            res += 1

    print(res)


if __name__ == "__main__":
    main()
