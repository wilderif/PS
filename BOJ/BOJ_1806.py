# BOJ_1806
# 부분합

import sys


def solution():
    n, s = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    res = n + 1
    p_1 = 0
    p_2 = 0
    cur_sum = arr[0]
    while True:
        if cur_sum < s:
            p_2 += 1
            if p_2 == n:
                break
            cur_sum += arr[p_2]
        elif cur_sum >= s and p_1 < p_2:
            if p_2 - p_1 + 1 < res:
                res = p_2 - p_1 + 1
            cur_sum -= arr[p_1]
            p_1 += 1
        elif cur_sum >= s and p_1 == p_2:
            if p_2 - p_1 + 1 < res:
                res = p_2 - p_1 + 1
            p_2 += 1
            if p_2 == n:
                break
            cur_sum += arr[p_2]

    if res == n + 1:
        print(0)
    else:
        print(res)


if __name__ == "__main__":
    solution()
