# BOJ_2573
# 빙산

import sys


def check(arr):
    vis = [[True for _ in range(m)] for _ in range(n)]
    ret = 0
    for j in range(n):
        for i in range(m):
            if arr[j][i] and vis[j][i]:
                ret += 1
                stack = []
                stack.append((j, i))
                vis[j][i] = False
                while stack:
                    cur = stack.pop()
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] and arr[nx][ny]:
                            vis[nx][ny] = False
                            stack.append((nx, ny))
    return ret


def melt(arr):
    to_melt = []
    for j in range(n):
        for i in range(m):
            if arr[j][i]:
                for d in range(4):
                    nx = j + dx[d]
                    ny = i + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                        to_melt.append((j, i))
    while to_melt:
        cur = to_melt.pop()
        if arr[cur[0]][cur[1]]:
            arr[cur[0]][cur[1]] -= 1


def main():
    global dx, dy, n, m
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    res = 0
    while True:
        ch = check(arr)
        if ch == 0:
            print(0)
            break
        if ch > 1:
            print(res)
            break
        res += 1
        melt(arr)


if __name__ == "__main__":
    main()
