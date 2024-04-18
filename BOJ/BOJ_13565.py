# BOJ_13565
# 침투

import sys


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    m, n = map(int, sys.stdin.readline().split())
    arr = [sys.stdin.readline().rstrip() for _ in range(m)]
    vis = [[True for _ in range(n)] for _ in range(m)]

    for i in range(n):
        if arr[0][i] == '0' and vis[0][i]:
            stack = []
            stack.append((0, i))
            vis[0][i] = False
            while stack:
                cur = stack.pop()
                for d in range(4):
                    nx = cur[0] + dx[d]
                    ny = cur[1] + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == '0' and vis[nx][ny]:
                        vis[nx][ny] = False
                        stack.append((nx, ny))
    for i in range(n):
        if vis[m - 1][i] == False:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
