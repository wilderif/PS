# BOJ_11123
# 양 한마리... 양 두마리...

import sys

inp = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    t = int(inp())
    for _ in range(t):
        h, w = map(int, inp().split())
        board = [inp().rstrip() for _ in range(h)]
        
        vis = [[False for _ in range(w)] for _ in range(h)]
        res = 0
        for i in range(h):
            for j in range(w):
                if board[i][j] == '#' and vis[i][j] is False:
                    res += 1
                    stack = [(i, j)]
                    vis[i][j] = True
                    while stack:
                        x, y = stack.pop()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and board[nx][ny] == '#':
                                stack.append((nx, ny))
                                vis[nx][ny] = True
        print(res)


if __name__ == "__main__":
    main()
