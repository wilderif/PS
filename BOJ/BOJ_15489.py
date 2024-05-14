# BOJ_15489
# 파스칼 삼각형

import sys


def solution():
    r, c, w = map(int, sys.stdin.readline().split())
    mem = [[0 for _ in range(r + w)] for _ in range(r + w)]
    for i in range(1, r + w):
        mem[i][1] = 1
        mem[i][i] = 1
    for i in range(3, r + w):
        for j in range(2, i):
            mem[i][j] = mem[i - 1][j - 1] + mem[i - 1][j]
    res = 0
    for i in range(r, r + w):
        for j in range(c, c + i - r + 1):
            res += mem[i][j]
    print(res)


if __name__ == "__main__":
    solution()