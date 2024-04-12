# BOJ_2589
# 보물섬

import sys
from collections import deque


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    r, c = map(int, sys.stdin.readline().split())
    arr = [sys.stdin.readline().rstrip() for _ in range(r)]

    res = 0
    for j in range(r):
        for i in range(c):
            if arr[j][i] == 'L':
                if 0 < j < r - 1 and arr[j - 1][i] == 'L' and arr[j + 1][i] == 'L':
                    continue
                if 0 < i < c - 1 and arr[j][i - 1] == 'L' and arr[j][i + 1] == 'L':
                    continue
                vis = [[-1 for _ in range(c)] for _ in range(r)]
                q = deque()
                q.append((j, i))
                vis[j][i] = 0
                tmp = 0
                while q:
                    cur = q.popleft()
                    cur_time = vis[cur[0]][cur[1]]
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 'L' and vis[nx][ny] == - 1:
                            vis[nx][ny] = cur_time + 1
                            tmp = max(tmp, cur_time + 1)
                            q.append((nx, ny))
                res = max(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
