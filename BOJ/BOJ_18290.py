# BOJ_18290
# NM과 K (1)

import sys

inp = sys.stdin.readline


def backtracking(start, count, ret):
    global res
    if count == k:
        res = max(res, ret)
        return

    if (k - count) * 10000 + ret < res:
        return

    for i in range(start[1] + 2, m):
        if start[0] > 0 and vis[start[0] - 1][i]:
            continue
        vis[start[0]][i] = True
        backtracking((start[0], i), count + 1, ret + board[start[0]][i])
        vis[start[0]][i] = False

    for i in range(start[0] + 1, n):
        for j in range(m):
            if vis[i - 1][j]:
                continue
            vis[i][j] = True
            backtracking((i, j), count + 1, ret + board[i][j])
            vis[i][j] = False


def main():
    global n, m, k, board, vis, res
    n, m, k = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]
    res = -10000 * 4

    for i in range(n):
        for j in range(m):
            vis[i][j] = True
            backtracking((i, j), 1, board[i][j])
            vis[i][j] = False

    print(res)


if __name__ == "__main__":
    main()
