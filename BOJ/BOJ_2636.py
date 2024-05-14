# BOJ_2636
# 치즈

import sys
from collections import deque


def bfs(arr):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    vis = [[True for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append((0, 0))
    vis[0][0] = False
    next = []
    while q:
        cur = q.popleft()
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < r and 0 <= ny < c and vis[nx][ny]:
                if arr[nx][ny]:
                    next.append((nx, ny))
                else:
                    q.append((nx, ny))
                vis[nx][ny] = False
    return next


def erase(arr, next):
    cnt = 0
    for c in next:
        if arr[c[0]][c[1]]:
            cnt += 1
            arr[c[0]][c[1]] = False
    return cnt


def main():
    global r, c
    r, c = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
    total_cheese = 0
    for j in range(r):
        for i in range(c):
            if arr[j][i]:
                total_cheese += 1
                arr[j][i] = True
            else:
                arr[j][i] = False
    
    res_cnt = 0
    res_remain = 0
    while total_cheese:
        tmp = erase(arr, bfs(arr))
        if total_cheese == tmp:
            res_remain = total_cheese
        total_cheese -= tmp
        res_cnt += 1
    print(res_cnt)
    print(res_remain)


if __name__ == "__main__":
    main()
