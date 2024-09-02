# BOJ_22342
# 계산 로봇

import sys

inp = sys.stdin.readline


def main():
    n, m = map(int, inp().split())
    board = [[0 for _ in range(m + 1)]] + [[0] + list(map(int, list(inp().rstrip()))) for _ in range(n)] + [[0 for _ in range(m + 1)]]
    mem = [[0 for _ in range(m + 1)] for _ in range(n + 2)]

    res = 0
    for i in range(1, m):
        for j in range(1, n + 1):
            mem[j][i] = max(mem[j - 1][i - 1], mem[j][i - 1], mem[j + 1][i - 1]) + board[j][i]
            res = max(res, mem[j][i])
    print(res)


if __name__ == "__main__":
    main()
