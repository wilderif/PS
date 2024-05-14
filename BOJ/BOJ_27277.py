# BOJ_27277
# 장기자랑

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    res = arr[n - 1]
    p1 = 0
    p2 = n - 2
    while p1 < p2:
        res += max(0, arr[p2] - arr[p1])
        p1 += 1
        p2 -= 1
    print(res)


if __name__ == "__main__":
    solution()
