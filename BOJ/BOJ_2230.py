# BOJ_2230
# 수 고르기

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = [int(sys.stdin.readline())for _ in range(n)]
    arr.sort()

    p1 = 0
    p2 = 1
    res = arr[n - 1] - arr[0]

    while p2 < n:
        if arr[p2] - arr[p1] < m:
            p2 += 1
        else:
            res = min(res, arr[p2] - arr[p1])
            p1 += 1
        if p1 == p2:
            p2 += 1

    print(res)


if __name__ == "__main__":
    solution()
