# BOJ_1303
# 전쟁 - 전투

import sys

inp = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n, m = map(int, inp().split())
    board = [inp().rstrip() for _ in range(m)]
    vis = [[False for _ in range(n)] for _ in range(m)]

    res1 = 0
    res2 = 0
    for i in range(m):
        for j in range(n):
            if vis[i][j]:
                continue
            cur_team = board[i][j]
            tmp = 1
            stack = [(i, j)]
            vis[i][j] = True
            while stack:
                x, y = stack.pop()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                        if board[nx][ny] == cur_team:
                            tmp += 1
                            vis[nx][ny] = True
                            stack.append((nx, ny))
            if cur_team == "W":
                res1 += tmp * tmp
            else:
                res2 += tmp * tmp
    print(res1, res2)


if __name__ == "__main__":
    main()
