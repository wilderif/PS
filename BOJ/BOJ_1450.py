# BOJ_1450
# 냅색문제

import sys
from itertools import combinations
import bisect

inp = sys.stdin.readline


def find_sum(arr):
    ret = []
    for i in range(len(arr) + 1):
        for com in combinations(arr, i):
            ret.append(sum(com))
    return ret


def main():
    n, c = map(int, inp().split())
    arr = list(map(int, inp().split()))

    sum1 = find_sum(arr[:n // 2])
    sum2 = sorted(find_sum(arr[n//2:]))

    res = 0
    for i in sum1:
        res += bisect.bisect_left(sum2, c - i + 1)

    print(res)


if __name__ == "__main__":
    main()
