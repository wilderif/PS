# BOJ_1026
# 보물

import sys


def solution():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort(reverse=True)

    res = 0
    for i in range(n):
        res += a[i] * b[i]

    print(res)


if __name__ == "__main__":
    solution()
