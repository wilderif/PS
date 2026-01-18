# BOJ_3010
# 페그

import sys

inp = sys.stdin.readline


def main():
    dirs_1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dirs_2 = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    board = [list(inp().rstrip().ljust(7)) for _ in range(7)]

    res = 0
    for i in range(7):
        for j in range(7):
            if board[i][j] != ".":
                continue
            for d in range(4):
                x_1, y_1 = i + dirs_1[d][0], j + dirs_1[d][1]
                x_2, y_2 = i + dirs_2[d][0], j + dirs_2[d][1]
                if not (0 <= x_2 < 7 and 0 <= y_2 < 7):
                    continue
                if board[x_2][y_2] != "o" or board[x_1][y_1] != "o":
                    continue
                res += 1
    print(res)


if __name__ == "__main__":
    main()
