# BOJ_6593
# 상범 빌딩

import sys
from collections import deque


def main():
    dx = (1, 0, 0, -1, 0, 0)
    dy = (0, 1, 0, 0, -1, 0)
    dz = (0, 0, 1, 0, 0, -1)
    while True:
        l, r, c = map(int, sys.stdin.readline().split())
        
        if not l and not r and not c:
            break
        
        start = None
        arr = list()
        for k in range(l):
            tmp = list()
            for j in range(r):
                tmp.append(sys.stdin.readline().rstrip())
                for i in range(c):
                    if tmp[j][i] == 'S':
                        start = (k, j ,i)
            sys.stdin.readline()
            arr.append(tmp)
        vis = [[[-1 for _ in range(c)] for _ in range(r)] for _ in range(l)]

        q = deque()
        q.append(start)
        vis[start[0]][start[1]][start[2]] = 0
        end_flag = False
        while q:
            if end_flag:
                q.clear()
                break
            cur = q.popleft()
            cur_time = vis[cur[0]][cur[1]][cur[2]]
            for d in range(6):
                nx = cur[0] + dx[d]
                ny = cur[1] + dy[d]
                nz = cur[2] + dz[d]
                if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                    if arr[nx][ny][nz] != '#' and vis[nx][ny][nz] == -1:
                        q.append((nx, ny, nz))
                        vis[nx][ny][nz] = cur_time + 1
                    if arr[nx][ny][nz] == 'E':
                        print(f"Escaped in {cur_time + 1} minute(s).")
                        end_flag = True
                        break
        else:
            print("Trapped!")


if __name__ == "__main__":
    main()
