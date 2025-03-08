# BOJ_1937
# 욕심쟁이 판다

import sys

sys.setrecursionlimit(10**4)

inp = sys.stdin.readline


def dfs(x, y):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if board[x][y] >= board[nx][ny]:
            continue
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


def main():
    global n, board, dp
    n = int(inp())
    board = [list(map(int, inp().split())) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dfs(i, j)

    res = 0
    for k in dp:
        res = max(res, max(k))
    print(res)


if __name__ == "__main__":
    main()
