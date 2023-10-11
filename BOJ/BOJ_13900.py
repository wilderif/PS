# BOJ_13900
# 순서쌍의 곱의 합

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    res = 0
    for i in range(n - 1):
        res += arr[i + 1] * arr[i]
        arr[i + 1] += arr[i]

    print(res)


if __name__ == "__main__":
    solution()
