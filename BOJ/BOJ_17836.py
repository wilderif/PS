# BOJ_17836
# 공주님을 구해라!

import sys

inp = sys.stdin.readline


def main():
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start, target):
        vis = [[False for _ in range(m)] for _ in range(n)]
        vis[start[0]][start[1]] = True
        q = [start]
        cnt = 0
        while q:
            nq = []
            cnt += 1
            for x, y in q:
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if board[nx][ny] == 1:
                        continue
                    if vis[nx][ny]:
                        continue
                    if (nx, ny) == target:
                        return cnt
                    vis[nx][ny] = True
                    nq.append((nx, ny))

            q = nq

        return 100 * 100 + 1

    n, m, t = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(n)]
    sword = None
    sword_to_end = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                sword = (i, j)
                sword_to_end = n - 1 - i + m - 1 - j
                break
        else:
            continue
        break

    res = min(bfs((0, 0), (n - 1, m - 1)), bfs((0, 0), sword) + sword_to_end)
    print(res if res <= t else "Fail")


if __name__ == "__main__":
    main()
