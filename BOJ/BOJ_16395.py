# BOJ_16395
# 파스칼의 삼각형

import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    mem = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mem[i][0] = 1
        mem[i][i] = 1

    for j in range(2, n):
        for i in range(1, j):
            mem[j][i] = mem[j - 1][i - 1] + mem[j - 1][i]

    print(mem[n - 1][k - 1])


if __name__ == "__main__":
    solution()
