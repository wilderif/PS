# BOJ_2491
# 수열

import sys


def solution():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    res_1 = 1
    res_1_c = 1
    res_2 = 1
    res_2_c = 1
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            res_1_c += 1
            res_2_c += 1
        elif arr[i] > arr[i + 1]:
            res_1_c += 1
            res_2_c = 1
        elif arr[i] < arr[i + 1]:
            res_2_c += 1
            res_1_c = 1
        if res_1 < res_1_c:
            res_1 = res_1_c
        if res_2 < res_2_c:
            res_2 = res_2_c

    print(max(res_1, res_2))


if __name__ == "__main__":
    solution()
