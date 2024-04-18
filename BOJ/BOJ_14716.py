# BOJ_14716
# 현수막

import sys


def main():
    dx = (-1, -1, -1, 1, 1, 1, 0, 0)
    dy = (-1, 0, 1, -1, 0, 1, -1, 1)
    m, n = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    vis = [[True for _ in range(n)] for _ in range(m)]

    res = 0
    for j in range(m):
        for i in range(n):
            if arr[j][i] and vis[j][i]:
                res += 1
                stack = []
                stack.append((j, i))
                vis[j][i] = False
                while stack:
                    cur = stack.pop()
                    for d in range(8):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] and vis[nx][ny]:
                            vis[nx][ny] = False
                            stack.append((nx, ny))
    print(res)


if __name__ == "__main__":
    main()
