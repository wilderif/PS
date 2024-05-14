# BOJ_1600
# 말이 되고픈 원숭이

import sys
from collections import deque

inp = sys.stdin.readline


def bfs():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    dx_h = (2, 2, 1, 1, -1, -1, -2, -2)
    dy_h = (-1, 1, -2, 2, -2, 2, -1, 1)

    vis = [[[-1, 0] for _ in range(w)] for _ in range(h)]
    q = deque()

    vis[0][0][0] = 0
    q.append((0, 0, 0))
    
    while vis[h - 1][w - 1][0] == -1:
        if not q:
            break
        cur = q.popleft()
        cur_time = vis[cur[0]][cur[1]][0]
        if cur[2] < k:
            for d in range(8):
                nx = cur[0] + dx_h[d]
                ny = cur[1] + dy_h[d]
                if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny]:
                    if vis[nx][ny][0] == -1 or vis[nx][ny][1] > cur[2] + 1:
                        vis[nx][ny][0] = cur_time + 1
                        vis[nx][ny][1] = cur[2] + 1
                        q.append((nx, ny, cur[2] + 1))
        for d in range(4):
            nx = cur[0] + dx[d]
            ny = cur[1] + dy[d]
            if 0 <= nx < h and 0 <= ny < w and not arr[nx][ny]:
                if vis[nx][ny][0] == -1 or vis[nx][ny][1] > cur[2]:
                    vis[nx][ny][0] = cur_time + 1
                    vis[nx][ny][1] = cur[2]
                    q.append((nx, ny, cur[2]))

    return vis[h - 1][w - 1][0]


def main():
    global k, w, h, arr
    k = int(inp())
    w, h = map(int, inp().split())
    arr = [list(map(int, inp().split())) for _ in range(h)]
    print(bfs())


if __name__ == "__main__":
    main()
