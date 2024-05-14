# BOJ_7562
# 나이트의 이동

import sys
from collections import deque


def main():
    dx = (-1, -2, -2, -1, 1, 2, 2, 1)
    dy = (2, 1, -1, -2, -2, -1, 1, 2)
    t = int(input())
    for _ in range(t):
        i = int(input())
        vis = [[-1 for _ in range(i)] for _ in range(i)]
        start = tuple(map(int, sys.stdin.readline().split()))
        end = tuple(map(int, sys.stdin.readline().split()))
        q = deque()
        q.append(start)
        vis[start[0]][start[1]] = 0
        while (vis[end[0]][end[1]] == -1):
            cur = q.popleft()
            cur_time = vis[cur[0]][cur[1]]
            for d in range(8):
                nx = cur[0] + dx[d]
                ny = cur[1] + dy[d]
                if 0 <= nx < i and 0 <= ny < i:
                    if vis[nx][ny] == -1:
                        q.append((nx, ny))
                        vis[nx][ny] = cur_time + 1
        print(vis[end[0]][end[1]])


if __name__ == "__main__":
    main()
