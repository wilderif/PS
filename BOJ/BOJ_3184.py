# BOJ_3184
# 양

import sys


def dfs(arr, vis, start):
    stack = list()
    stack.append(start)
    vis[start[0]][start[1]] = False
    res_o, res_v = 0, 0

    while stack:
        cur = stack.pop()
        if arr[cur[0]][cur[1]] == 'o':
            res_o += 1
        if arr[cur[0]][cur[1]] == 'v':
            res_v += 1
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < r and 0 <= ny < c and vis[nx][ny] and arr[nx][ny] != '#':
                vis[nx][ny] = False
                stack.append((nx, ny))
    if res_o > res_v:
        return res_o, 0
    else:
        return 0, res_v


def main():
    global dx, dy, r, c
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    r, c = map(int, sys.stdin.readline().split())
    arr = [sys.stdin.readline().rstrip() for _ in range(r)]
    vis = [[True for _ in range(c)] for _ in range(r)]

    res_o, res_v = 0, 0
    for j in range(r):
        for i in range(c):
            if vis[j][i] and arr[j][i] != '#':
                res = dfs(arr, vis, (j, i))
                res_o += res[0]
                res_v += res[1]
    print(res_o, res_v)


if __name__ == "__main__":
    main()
