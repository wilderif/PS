# BOJ_2146
# 다리 만들기

import sys
from collections import deque

inp = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n = int(inp())
    arr = [list(map(int, inp().split())) for _ in range(n)]
    mapping = 2
    for i in range(n):
        for j in range(n):
            if arr[j][i] == 1:
                q = deque()
                q.append((j, i))
                arr[j][i] = mapping
                while q:
                    cur = q.popleft()
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                            arr[nx][ny] = mapping
                            q.append((nx, ny))
                mapping += 1
    
    vis = [[True for _ in range(n)] for _ in range(n)]
    start = []
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                q = deque()
                q.append((j, i))
                vis[j][i] = False
                while q:
                    cur = q.popleft()
                    for d in range(4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not arr[nx][ny] and vis[nx][ny]:
                                vis[nx][ny] = False
                                q.append((nx, ny))
                            if 0 < arr[nx][ny] < mapping - 1 and vis[nx][ny]:
                                vis[nx][ny] = False
                                start.append((nx, ny, arr[nx][ny]))
                break

    res = 100 * 100
    while start:
        vis = [[-1 for _ in range(n)] for _ in range(n)]
        flag = False
        q = deque()
        starting = start.pop()
        q.append((starting[0], starting[1]))
        vis[starting[0]][starting[1]] = 0
        while q:
            cur = q.popleft()
            cur_time = vis[cur[0]][cur[1]]
            for d in range(4):
                nx = cur[0] + dx[d]
                ny = cur[1] + dy[d]
                if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] == -1:
                    if not arr[nx][ny]:
                        vis[nx][ny] = cur_time + 1
                        q.append((nx, ny))
                    if arr[nx][ny] > starting[2]:
                        res = min(res, cur_time)
                        flag = True
                        break
            if flag:
                break
    print(res)

        
if __name__ == "__main__":
    main()
