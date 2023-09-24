# BOJ_1461
# 도서관

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_p = []
    arr_n = []

    for i in arr:
        if i < 0:
            arr_n.append(i)
        else:
            arr_p.append(i)
    arr_p.sort(reverse=True)
    arr_n.sort()

    res = 0
    for i in range(0, len(arr_p), m):
        res += arr_p[i] * 2
    for i in range(0, len(arr_n), m):
        res += -arr_n[i] * 2

    if len(arr_p) == 0:
        res -= -arr_n[0]
    elif len(arr_n) == 0:
        res -= arr_p[0]
    elif -arr_n[0] >= arr_p[0]:
        res -= -arr_n[0]
    else:
        res -= arr_p[0]

    print(res)


if __name__ == "__main__":
    solution()
