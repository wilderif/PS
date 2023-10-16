# BOJ_3273
# 두 수의 합

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    x = int(sys.stdin.readline())
    arr.sort()
    p_1 = 0
    p_2 = n - 1
    res = 0

    while True:
        if p_1 == p_2:
            break
        if arr[p_1] + arr[p_2] > x:
            p_2 -= 1
        elif arr[p_1] + arr[p_2] == x:
            res += 1
            p_1 += 1
        else:
            p_1 += 1

    print(res)


if __name__ == "__main__":
    solution()
