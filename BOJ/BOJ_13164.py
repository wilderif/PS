# BOJ_13164
# 행복 유치원


import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    arr_p = list(map(int, sys.stdin.readline().split()))
    arr_d = []
    for i in range(1, n):
        arr_d.append(arr_p[i] - arr_p[i - 1])

    arr_d.sort(reverse=True)

    res = 0
    for i in range(k - 1, n - 1):
        res += arr_d[i]
    print(res)


if __name__ == "__main__":
    solution()
