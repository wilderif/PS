# BOJ_14502
# 연구소

import sys

inp = sys.stdin.readline


def dfs():
    global res
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    vis = [[True for _ in range(m)] for _ in range(n)]
    stack = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                stack.append((i, j))
                vis[i][j] = False
                cnt += 1
                while stack:
                    cur = stack.pop()
                    for d in range(4):
                        nx, ny = cur[0] + dx[d], cur[1] + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny] and vis[nx][ny]:
                            stack.append((nx, ny))
                            vis[nx][ny] = False
                            cnt += 1
    res = min(res, cnt)
                            

def backtracking(count, x, y):
    if count == 3:
        dfs()
        return
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                backtracking(count + 1, i, j)
                arr[i][j] = 0
    


def main():
    global n, m, arr, res
    n, m = map(int, inp().split())
    arr = [list(map(int, inp().split())) for _ in range(n)]
    res = 8 * 8
    backtracking(0, 0, 0)
    empty = 0
    initial_virus = 0
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                empty += 1
            if arr[i][j] == 2:
                initial_virus += 1
    print(empty - res + initial_virus - 3)

    
if __name__ == "__main__":
    main()
