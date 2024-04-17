# BOJ_2468
# 안전 영역

import sys


def dfs(depth, arr, vis, start):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    stack = []
    stack.append(start)
    vis[start[0]][start[1]] = False
    while stack:
        cur = stack.pop()
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] and arr[nx][ny]> depth:
                vis[nx][ny] = False
                stack.append((nx, ny))


def check(depth, arr):
    ret = 0
    vis = [[True for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if arr[j][i] > depth and vis[j][i]:
                ret += 1
                dfs(depth, arr, vis, (j, i))
    return ret


def main():
    global n
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    max_arr = 0
    for i in arr:
        max_arr = max(max_arr, max(i))
    res = 0
    for i in range(max_arr + 1):
        res = max(res, check(i, arr))
    print(res)


if __name__ == "__main__":
    main()
