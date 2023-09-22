# BOJ_1010
# 다리 놓기

import sys


def solution():
    mem = [[0 for _ in range(30)] for _ in range(30)]
    mem[1][0] = 1
    mem[1][1] = 1

    for i in range(30):
        mem[i][0] = 1
        mem[i][i] = 1

    for i in range(2, 30):
        for j in range(1, i + 1):
            mem[i][j] = mem[i - 1][j] + mem[i - 1][j - 1]

    n = int(input())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        print(mem[b][a])


if __name__ == "__main__":
    solution()
