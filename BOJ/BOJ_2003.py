# BOJ_2003
# 수들의 합 2

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    p_1 = 0
    p_2 = 0
    res = 0
    cur_sum = arr[0]
    while True:
        if cur_sum == m:
            res += 1
        if cur_sum <= m:
            p_2 += 1
            if p_2 == n:
                break
            cur_sum += arr[p_2]
        elif cur_sum > m and p_1 < p_2:
            cur_sum -= arr[p_1]
            p_1 += 1
        elif cur_sum > m and p_1 == p_2:
            p_1 += 1
            p_2 += 1
            if p_2 == n:
                break
            cur_sum = arr[p_1]

    print(res)


if __name__ == "__main__":
    solution()
