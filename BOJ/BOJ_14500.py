# BOJ_14500
# 테트로미노

import sys

inp = sys.stdin.readline

def dfs(x, y, cnt, c_sum):
    global res
    if c_sum + (4 - cnt) * arr_max < res:
        return
    if cnt == 4:
        res = max(res, c_sum)
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n  and 0 <= ny < m and vis[nx][ny]:
            vis[nx][ny] = False
            dfs(nx, ny, cnt + 1, c_sum + arr[nx][ny])
            vis[nx][ny] = True


def differ_shape(x, y):
    global res
    tmp = []
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            tmp.append(arr[nx][ny])
    if len(tmp) < 3:
        return
    tmp.sort(reverse=True)
    res = max(res, sum(tmp[:3]) + arr[x][y])


def main():
    global dx, dy, n, m, arr, vis, res, arr_max
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    n, m = map(int, inp().split())
    arr = [list(map(int, inp().split())) for _ in range(n)]
    vis = [[True for _ in range(m)] for _ in range(n)]

    arr_max = max(map(max, arr))

    global res
    res = 0
    for i in range(n):
        for j in range(m):
            vis[i][j] = False
            dfs(i, j, 1, arr[i][j])
            vis[i][j] = True
            differ_shape(i, j)
    print(res)
                
    
if __name__ == "__main__":
    main()
