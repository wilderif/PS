# BOJ_5958
# Space Exploration

import sys

inp = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n = int(inp())
    board = [inp().strip() for _ in range(n)]
    vis = [[False for _ in range(n)] for _ in range(n)]

    res = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*' and not vis[i][j]:
                res += 1
                vis[i][j] = True
                stack = [(i, j)]
                while stack:
                    cur = stack.pop()
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == '*' and not vis[nx][ny]:
                                vis[nx][ny] = True
                                stack.append((nx, ny))
    print(res)


if __name__ == "__main__":
    main()
