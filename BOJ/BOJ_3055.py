# BOJ_3055
# 탈출

import sys

inp = sys.stdin.readline


def main():
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    r, c = map(int, inp().split())
    board = [list(inp().strip()) for _ in range(r)]
    can_vis = [[True] * c for _ in range(r)]
    water = []
    beaver = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                water.append((i, j))
                can_vis[i][j] = False
            if board[i][j] == 'S':
                beaver.append((i, j, 0))
                can_vis[i][j] = False
            if board[i][j] == 'X':
                can_vis[i][j] = False

    while water or beaver:
        new_water = []
        for x, y in water:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < r and 0 <= ny < c and can_vis[nx][ny]:
                    if board[nx][ny] == 'D':
                        continue
                    can_vis[nx][ny] = False
                    new_water.append((nx, ny))
        water = new_water

        new_beaver = []
        for i in beaver:
            for d in range(4):
                nx = i[0] + dx[d]
                ny = i[1] + dy[d]
                if 0 <= nx < r and 0 <= ny < c and can_vis[nx][ny]:
                    if board[nx][ny] == 'D':
                        print(i[2] + 1)
                        return
                    can_vis[nx][ny] = False
                    new_beaver.append((nx, ny, i[2] + 1))
        beaver = new_beaver
    print("KAKTUS")


if __name__ == "__main__":
    main()
