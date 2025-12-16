# 리코쳇_로봇


def solution(board):
    n, m = len(board), len(board[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start, target = None, None

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i, j)
            if board[i][j] == "G":
                target = (i, j)

    def bfs(s, e):
        q = [s]
        cnt = 0
        vis = [[False for _ in range(m)] for _ in range(n)]
        vis[s[0]][s[1]] = True

        while q:
            cnt += 1
            nq = []
            for x, y in q:
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == "D":
                        continue
                    while True:
                        tx, ty = nx + dx, ny + dy
                        if not (0 <= tx < n and 0 <= ty < m):
                            break
                        if board[tx][ty] == "D":
                            break
                        nx, ny = tx, ty
                    if vis[nx][ny]:
                        continue
                    if e == (nx, ny):
                        return cnt
                    nq.append((nx, ny))
                    vis[nx][ny] = True
            q = nq

        return -1

    return bfs(start, target)
