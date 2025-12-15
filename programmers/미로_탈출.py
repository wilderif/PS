# 미로_탈출


def solution(maps):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    n, m = len(maps), len(maps[0])

    def bfs(s, e):
        vis = [[False for _ in range(m)] for _ in range(n)]
        queue = [s]
        vis[s[0]][s[1]] = True
        cnt = 0

        while queue:
            cnt += 1
            new_queue = []

            for x, y in queue:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if vis[nx][ny]:
                        continue
                    if maps[nx][ny] == "X":
                        continue
                    if (nx, ny) == e:
                        return cnt
                    vis[nx][ny] = True
                    new_queue.append((nx, ny))

            queue = new_queue

        return -1

    start, lever, exit = None, None, None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            if maps[i][j] == "L":
                lever = (i, j)
            if maps[i][j] == "E":
                exit = (i, j)

    to_lever = bfs(start, lever)
    to_exit = bfs(lever, exit)

    return -1 if to_lever == -1 or to_exit == -1 else to_lever + to_exit
