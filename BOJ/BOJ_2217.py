# BOJ_2217
# 로프

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    arr.sort()

    res = 0
    for i in range(n):
        if arr[i] * (n - i) > res:
            res = arr[i] * (n - i)
    print(res)


if __name__ == "__main__":
    solution()
