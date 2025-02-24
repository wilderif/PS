# BOJ_5573
# 산책

import sys

inp = sys.stdin.readline


def main():
    h, w, n = map(int, inp().split())
    board = [list(map(int, inp().split())) for _ in range(h)]
    dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    dp[0][0] = n - 1
    for i in range(h):
        for j in range(w):
            if dp[i][j] % 2:
                if board[i][j]:
                    dp[i + 1][j] += dp[i][j] // 2
                    dp[i][j + 1] += dp[i][j] // 2 + 1
                else:
                    dp[i + 1][j] += dp[i][j] // 2 + 1
                    dp[i][j + 1] += dp[i][j] // 2
            else:
                dp[i + 1][j] += dp[i][j] // 2
                dp[i][j + 1] += dp[i][j] // 2

    coord = [0, 0]
    while coord[0] < h and coord[1] < w:
        if dp[coord[0]][coord[1]] % 2:
            if board[coord[0]][coord[1]]:
                coord[0] += 1
            else:
                coord[1] += 1
        else:
            if board[coord[0]][coord[1]]:
                coord[1] += 1
            else:
                coord[0] += 1
    print(coord[0] + 1, coord[1] + 1)


if __name__ == "__main__":
    main()
