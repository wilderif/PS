# BOJ_11048
# 이동하기

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(m + 2)]]
    for _ in range(n):
        arr.append([0] + list(map(int, sys.stdin.readline().split() + [0])))
    arr.append([0 for _ in range(m + 2)])
    mem = [[0 for _ in range(m + 2)] for _ in range(n + 2)]

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            mem[j][i] = max(mem[j - 1][i - 1], mem[j][i - 1], mem[j - 1][i]) + arr[j][i]

    print(mem[n][m])


if __name__ == "__main__":
    solution()
