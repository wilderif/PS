# BOJ_31246
# 모바일 광고 입찰

import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    arr = list()
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if a - b >= 0:
            k -= 1
        else:
            arr.append(b - a)
    if k <= 0:
        print(0)
    else:
        arr.sort()
        print(arr[k - 1])


if __name__ == "__main__":
    solution()
