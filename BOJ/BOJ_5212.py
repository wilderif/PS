# BOJ_5212
# 지구 온난화

import sys

inp = sys.stdin.readline


def main():
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    r, c = map(int, inp().split())
    board = [list(inp().rstrip()) for _ in range(r)]
    del_arr = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                continue
            cnt = 0
            for dx, dy in dirs:
                nx = i + dx
                ny = j + dy
                if (0 <= nx < r and 0 <= ny < c) and board[nx][ny] == "X":
                    continue
                cnt += 1
            if cnt >= 3:
                del_arr.append((i, j))

    for x, y in del_arr:
        board[x][y] = "."

    x_range = [0, r]
    y_range = [0, c]
    for i in range(r):
        if "X" in board[i]:
            x_range[0] = i
            break

    for i in range(r - 1, -1, -1):
        if "X" in board[i]:
            x_range[1] = i + 1
            break

    for j in range(c):
        for i in range(r):
            if board[i][j] == "X":
                y_range[0] = j
                break
        else:
            continue
        break

    for j in range(c - 1, -1, -1):
        for i in range(r):
            if board[i][j] == "X":
                y_range[1] = j + 1
                break
        else:
            continue
        break

    for x in range(*x_range):
        for y in range(*y_range):
            print(board[x][y], end="")
        print()


if __name__ == "__main__":
    main()
