# BOJ_1890
# 점프

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    mem = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if j == 0 and i == 0:
                if i + arr[j][i] < n:
                    mem[j][i + arr[j][i]] += 1
                if j + arr[j][i] < n:
                    mem[j + arr[j][i]][i] += 1
            elif j == n - 1 and i == n - 1:
                break
            else:
                if i + arr[j][i] < n and mem[j][i] != 0:
                    mem[j][i + arr[j][i]] += mem[j][i]
                if j + arr[j][i] < n and mem[j][i] != 0:
                    mem[j + arr[j][i]][i] += mem[j][i]

    print(mem[n - 1][n - 1])


if __name__ == "__main__":
    solution()
