# 석유_시추


def solution(land):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    r = len(land)
    c = len(land[0])

    res = [0 for _ in range(c)]
    vis = [[False for _ in range(c)] for _ in range(r)]

    def dfs(start):
        used = set()
        cnt = 1
        stack = [start]
        used.add(start[1])
        vis[start[0]][start[1]] = True

        while stack:
            cx, cy = stack.pop()
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]

                if not (0 <= nx < r and 0 <= ny < c):
                    continue
                if not land[nx][ny]:
                    continue
                if vis[nx][ny]:
                    continue
                cnt += 1
                vis[nx][ny] = True
                stack.append((nx, ny))
                used.add(ny)

        return used, cnt

    for i in range(r):
        for j in range(c):
            if land[i][j] and not vis[i][j]:
                used, cnt = dfs((i, j))
                for k in used:
                    res[k] += cnt
                    pass

    return max(res)
