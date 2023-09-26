# BOJ_1932
# 정수 삼각형

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    mem = [[0 for _ in range(n)] for _ in range(n)]
    mem[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            mem[i][j] = max(mem[i + 1][j] + arr[i][j], mem[i + 1][j + 1] + arr[i][j])

    print(mem[0][0])


if __name__ == "__main__":
    solution()
