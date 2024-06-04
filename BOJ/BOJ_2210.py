# BOJ_2210
# 숫자판 점프

import sys

inp = sys.stdin.readline


def dfs(board, res, start):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    stack = []
    stack.append(start)
    while stack:
        x, y, path = stack.pop()
        if len(path) == 6:
            res.add(path)
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5:
                stack.append((nx, ny, path + board[nx][ny]))


def main():
    board = [list(inp().split()) for _ in range(5)]
    res = set()
    for i in range(5):
        for j in range(5):
            dfs(board, res, (i, j, board[i][j]))
    print(len(res))


if __name__ == "__main__":
    main()
