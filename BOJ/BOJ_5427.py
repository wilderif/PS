# BOJ_5427
# 불

import sys
from collections import deque


def bfs(vis, arr, q, sk_check):
    while q:
        cur = q.popleft()
        cur_time = vis[cur[0]][cur[1]]
        if sk_check:
            if cur[0] == 0 or cur[0] == h - 1 or cur[1] == 0 or cur[1] == w - 1:
                return cur_time + 1
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] != '#':
                    if vis[nx][ny] == -1 or cur_time + 1 < vis[nx][ny]:
                        vis[nx][ny] = cur_time + 1
                        q.append((nx, ny, cur_time + 1))

    else:
        return "IMPOSSIBLE"


def main():
    global dx, dy
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    t = int(sys.stdin.readline())
    for _ in range(t):
        global w, h
        w, h = map(int, sys.stdin.readline().split())
        arr = list()
        vis = [[-1 for _ in range(w)] for _ in range(h)]
        q_fire = deque()
        q_sk = deque()
        for j in range(h):
            arr.append(list(sys.stdin.readline().strip()))
            for i in range(w):
                if arr[j][i] == '*':
                    vis[j][i] = 0
                    q_fire.append((j, i))
                if arr[j][i] == '@':
                    q_sk.append((j, i))
        
        bfs(vis, arr, q_fire, False)
        vis[q_sk[0][0]][q_sk[0][1]] = 0
        print(bfs(vis, arr, q_sk, True))


if __name__ == "__main__":
    main()
