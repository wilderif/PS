# BOJ_16946
# 벽 부수고 이동하기 4

import sys

inp = sys.stdin.readline


def empty_size(board, vis, x, y, id):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    to_fill = 0
    stack = []
    stack.append((x, y))
    vis[x][y] = id

    while stack:
        to_fill += 1
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] == 0 and board[nx][ny] == 0:
                stack.append((nx, ny))
                vis[nx][ny] = id
    return to_fill


def get_res(vis, res, group):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                tmp = 1
                used_id = set()
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n  and 0 <= ny < m and vis[nx][ny] and vis[nx][ny] not in used_id:
                        tmp += group[vis[nx][ny]]
                        used_id.add(vis[nx][ny])
                res[i][j] = tmp % 10

    

def main():
    global n, m
    n, m = map(int, inp().split())
    board = [list(map(int, inp().strip())) for _ in range(n)]
    vis = [[0 for _ in range(m)] for _ in range(n)]
    group = [0]
    id = 1
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                vis[i][j] = 0
            else:
                if not vis[i][j]:
                    group.append(empty_size(board, vis, i, j, id))
                    id += 1
    
    res  = [[0 for _ in range(m)] for _ in range(n)]
    get_res(vis, res, group)
    for line in res:
        print("".join(map(str, line)))


if __name__ == "__main__":
    main()
