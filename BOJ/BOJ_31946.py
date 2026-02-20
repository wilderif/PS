# BOJ_31946
# 죽음의 등굣길

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    m = int(inp())
    board = [list(map(int, inp().split())) for _ in range(n)]
    x = int(inp())

    if board[0][0] != board[-1][-1]:
        print("DEAD")
        return

    if board[0][0] == 1:
        for i in range(n):
            for j in range(m):
                board[i][j] = (board[i][j] + 1) % 2

    def find_next(cur):
        ret = []
        for i in range(x + 1):
            for j in range(x - i + 1):
                ret.append((cur[0] - i, cur[1] - j))
                ret.append((cur[0] - i, cur[1] + j))
                ret.append((cur[0] + i, cur[1] - j))
                ret.append((cur[0] + i, cur[1] + j))

        return ret

    vis = [[False for _ in range(m)] for _ in range(n)]
    stack = [(0, 0)]
    vis[0][0] = True
    while stack:
        cur = stack.pop()
        for nx, ny in find_next(cur):
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if board[nx][ny]:
                continue
            if vis[nx][ny]:
                continue
            if nx == n - 1 and ny == m - 1:
                print("ALIVE")
                return
            vis[nx][ny] = True
            stack.append((nx, ny))

    print("DEAD")


if __name__ == "__main__":
    main()
