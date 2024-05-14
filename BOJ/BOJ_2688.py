# BOJ_2688
# 줄어들지 않아

import sys


def solution():
    t = int(sys.stdin.readline())
    mem = [[0 for _ in range(10)] for _ in range(66)]

    for i in range(10):
        mem[1][i] = 1
    for i in range(1, 66):
        mem[i][0] = 1

    for i in range(2, 66):
        for j in range(1, 10):
            mem[i][j] = mem[i - 1][j] + mem[i][j - 1]

    for _ in range(t):
        n = int(sys.stdin.readline())
        print(mem[n + 1][9])


if __name__ == "__main__":
    solution()
