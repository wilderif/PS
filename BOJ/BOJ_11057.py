# BOJ_11057
# 오르막 수

import sys


def solution():
    n = int(sys.stdin.readline())
    mem = [[0 for _ in range(10)] for _ in range(n + 1)]

    for i in range(10):
        mem[1][i] = 1
    for i in range(1, n + 1):
        mem[i][0] = 1

    for i in range(2, n + 1):
        for j in range(1, 10):
            mem[i][j] = (mem[i - 1][j] + mem[i][j - 1]) % 10007

    res = 0
    for i in mem[n]:
        res += i
    print(res % 10007)


if __name__ == "__main__":
    solution()
