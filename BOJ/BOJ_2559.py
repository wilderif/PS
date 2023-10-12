# BOJ_2559
# 수열

import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    cur = 0
    for i in range(k):
        cur += arr[i]
    res = cur
    for i in range(1, n - k + 1):
        cur -= arr[i - 1]
        cur += arr[i + k - 1]

        if cur > res:
            res = cur

    print(res)


if __name__ == "__main__":
    solution()
