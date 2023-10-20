# BOJ_1246
# 온라인 판매

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = [int(sys.stdin.readline()) for _ in range(m)]
    arr.sort()
    if n < m:
        arr = arr[m - n:]

    idx = 0
    res = 0
    for i in range(len(arr)):
        if arr[i] * (len(arr) - i) > res:
            res = arr[i] * (len(arr) - i)
            idx = i

    print(arr[idx], end=' ')
    print(res)


if __name__ == "__main__":
    solution()
